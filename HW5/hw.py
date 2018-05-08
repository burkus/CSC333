#! python
# HW5
from qDES import *
from random import randrange
# Meet in the middle attack
r = 2 ** 16
def mithm(pairs):
    #ct1 decrypted = pt1 encrypted on key k
    pt = pairs[0][0]
    ct = pairs[0][1]
    encryptionMap = getPlaintextEncryptions(pt, r)
    decryptionMap = getCiphertextDecryptions(ct, r)

    keyPairs = []
    for k1, ct in encryptionMap.items():
        for k2, pt in decryptionMap.items():
            if ct == pt:
                pair = (k1, k2)
                keyPairs.append(pair)

    pt2 = pairs[1][0]
    ct2 = pairs[1][1]
    keys = []
    for pair in keyPairs:
        k1 = pair[0]
        k2 = pair[1]
        if qtD(ct2, k2) == qtE(pt2, k1):
            keys.append((k1, k2))
    return keys


def getPlaintextEncryptions(pt, r):
    map = {}
    for k in range(r):
        encryption = qtE(pt, k)
        map[k] = encryption
    return map

def getCiphertextDecryptions(ct, r):
    map = {}
    for k in range(r):
        decryption = qtD(ct, k)
        map[k] = decryption
    return map

def testMithm():
    k1 = randrange(r)
    k2 = randrange(r)
    pt1 = 12345
    pt2 = 5678
    ct1 = qtE(qtE(pt1, k1), k2)
    ct2 = qtE(qtE(pt2, k1), k2)
    startTime = clock()
    keysFound = mithm([(pt1, ct1), (pt2, ct2)])
    endTime = clock()
    print("Keys used: ", end="")
    print(k1, k2, sep=", ")
    print("Keys found: ")
    for pair in keysFound:
        print(pair[0], pair[1], sep=", ")
    print("Time Elasped: " + str(endTime - startTime) + " seconds")
