#! python
# HW5
from qDES import *
from random import randrange
# Meet in the middle attack
r = 2 ** 16
def mithm(pairs):
    #ct1 decrypted = pt1 encrypted on key k
    pt, ct = pairs[0]
    encryptionMap = getPlaintextEncryptions(pt, r)
    decryptionMap = getCiphertextDecryptions(ct, r)

    keyPairs = []
    for ct, k1s in encryptionMap.items():
        if ct in decryptionMap.keys():
            k2s = decryptionMap[ct]
            for k1 in k1s:
                for k2 in k2s:
                    keyPairs.append((k1, k2))

    for pair in pairs[1:]:
        pti, cti = pair
        keys = []
        for pair in keyPairs:
            k1, k2 = pair
            if qtD(cti, k2) == qtE(pti, k1):
                keys.append((k1, k2))
    return keys


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

def testMithm():
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
    print("Keys used: ", end="")
    print(k1, k2, sep=", ")
    print("Keys found: ")
    for pair in keysFound:
        print(pair[0], pair[1], sep=", ")
    print("Time Elasped: " + str(endTime - startTime) + " seconds")

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

def bruteForcePair(pair):
    pt, ct = pair
    for k in range(2**16):
        ctp = qtE(pt, k)
        k2 = ctp ^ ct
        if k2 ^ ctp == ct:
            return (k, k2)

pairs = ((81273, 54174), (2785, 44313), (90135, 18467))

def bruteForcePairs(pairs):
    for pair in pairs:
        pt, ct = pair
        keys = bruteForcePair(pair)
        print()
        print("(k1, k2) = " + str(keys))
        print("Double Checking Keys...")
        k1, k2 = keys
        output = impqtE(pt, k1, k2)
        if output == ct:
            print("Keys are correct")
            print("(pt, ct) =", pair)
            print("impqtE({}, {}, {}) = {}".format(pt, k1, k2, output))
        else:
            print("RIP.")
