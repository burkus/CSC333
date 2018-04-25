from quarterDES import *
from random import randrange

def testrun(n):
    k = randrange(2 ** 16)
    pt = randrange(2 ** 16)
    startTime = clock()
    for _ in range(n):
        qtE(pt, k)
    endTime = clock()
    deltaTime = endTime - startTime
    deltaTime *= (10 ** 3)
    print("Runtime for " + str(n) + " tests was:{:10.3f}ms".format(deltaTime))
    print("Average runtime for a single encryption is:", end='')
    averageTime = deltaTime / n
    print("{:10.3f}ms".format(averageTime))

def bruteForcePairs(pairs):
    keys = []
    for pair in pairs:
        keys.append(bruteForcePair(pair))
    return keys

def bruteForcePair(pair):
    keyRange = 2 ** 16
    pt = pair[0]
    ct = pair[1]
    keys = []
    for k in range(keyRange):
        output = qtE(pt, k)
        if output == ct:
            keys.append(k)
    return keys

def createPairs(n, r):
    pairs = []
    for _ in range(n):
        pt = randrange(r)
        k = randrange(r)
        ct = qtE(pt, k)
        pair = (pt, ct, k)
        pairs.append(pair)
    return pairs

def testBruteForceWithNumberOfPairs(n):
    pairs = createPairs(n, 2**16)
    keys = bruteForcePairs(pairs)
    for i, pair in enumerate(pairs):
        pt, ct, k = pair
        print("pt:{:d}, ct:{:d}, k:{:d}; ".format(pt, ct, k))
        keyGroup = keys[i]
        print("keys found:", end='')
        for i, key in enumerate(keyGroup):
            print(" {:d} ".format(key), end='')
            if i + 1 == len(keyGroup):
                print("")

k = randrange(2 ** 16)
pt1 = randrange(2 ** 16)
pt2 = randrange(2 ** 16)
ct1 = qtE(pt1, k)
ct2 = qtE(pt2, k)
