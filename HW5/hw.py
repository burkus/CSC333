#! python
# HW5
from qDES import *
from random import randrange
# Meet in the middle attack
r = 2 ** 16

def mithm(pairs):
    pt, ct = pairs[0]
    encryptionMap = getPlaintextEncryptions(pt, r)
    candidatePairs = []
    for k in range(r):
        decryption = qtD(ct, k)
        if decryption in encryptionMap.keys():
            k1s = encryptionMap[decryption]
            for k1 in k1s:
                candidatePairs.append((k1, k))

    keys = []
    for kp in candidatePairs:
        k1, k2 = kp
        works = True
        for pair in pairs:
            pt, ct = pair
            if qtD(ct, k2) != qtE(pt, k1):
                works = False
                break
        if works:
            keys.append(kp)
    return keys

def mithm0(pairs):
    pt, ct = pairs[0]
    encryptionMap = getPlaintextEncryptions(pt, r)
    candidatePairs = []
    for k in range(r):
        decryption = qtD(ct, k)
        if decryption in encryptionMap.keys():
            k1s = encryptionMap[decryption]
            for k1 in k1s:
                candidatePairs.append((k1, k))

    def filterCandidates(candidatePairs, pairs):
        if len(pairs) == 0:
            return candidatePairs

        pt, ct = pairs[0]
        f = lambda kp: qtD(ct, kp[1]) == qtE(pt, kp[0])
        filteredCandidatePairs = filter(f, candidatePairs)
        return filterCandidates(filteredCandidatePairs, pairs[1:])

    return filterCandidates(candidatePairs, pairs[1:])

def getPlaintextEncryptions(pt, r):
    map = {}
    for k in range(r):
        encryption = qtE(pt, k)
        if encryption in map.keys():
            map[encryption].append(k)
        else:
            map[encryption] = [k]
    return map

def getCiphertextDecryptions(ct, r):
    map = {}
    for k in range(r):
        decryption = qtD(ct, k)
        if decryption in map.keys():
            map[decryption].append(k)
        else:
            map[decryption] = [k]
    return map

def testMithm(mithm):
    k1 = randrange(r)
    k2 = randrange(r)
    pt1 = 12345
    pt2 = 5678
    pt3 = 4352
    ct1 = qtE(qtE(pt1, k1), k2)
    ct2 = qtE(qtE(pt2, k1), k2)
    ct3 = qtE(qtE(pt3, k1), k2)
    startTime = clock()
    keysFound = mithm([(pt1, ct1), (pt2, ct2), (pt3, ct3)])
    endTime = clock()
    print("Time Elasped: " + str(endTime - startTime) + " seconds")
    print("Keys used: ", end="")
    print(k1, k2, sep=", ")
    print("Keys found: ")
    for pair in keysFound:
        print(pair[0], pair[1], sep=", ")

def testMithmWithPairs(pairs):
    startTime = clock()
    keysFound = mithm(pairs)
    endTime = clock()
    print("Keys found: ")
    for pair in keysFound:
        print(pair[0], pair[1], sep=", ")
    print("Time Elasped: " + str(endTime - startTime) + " seconds")

    for keys in keysFound:
        k1 = keys[0]
        k2 = keys[1]
        works = 0
        for pair in pairs:
            pt = pair[0]
            ct = pair[1]
            if qtD(ct, k2) == qtE(pt, k1):
                works += 1
            if works == 3:
                return (k1, k2)

def bruteForcePairs(pairs):
    pt, ct = pairs[0]
    keys = []
    for k in range(2**16):
        ctp = qtE(pt, k)
        k2 = ctp ^ ct
        works = True
        for pair in pairs[1:]:
            pt, ct = pair
            if impqtE(pt, k, k2) != ct:
                works = False
        if works:
            keys.append((k, k2))
    return keys


pairs = ((81273, 54174), (2785, 44313), (90135, 18467))
