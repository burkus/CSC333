from quarterDES import *
from random import randrange

def testrun(n):
    k = randrange(2 ** 16)
    pt = randrange(2 ** 16)
    startTime = clock()
    for _ in range(n):
        qtE(pt, k)
    endTime = clock()
    deltaTime = endTime = startTime
    deltaTime *= 10 ** 3
    print("Runtime for " + str(n) + " tests was:{:10.3f}ms".format(deltaTime))
    print("Average runtime for a single encryption is:", end='')
    averageTime = deltaTime / n
    print("{:10.3f}ms".format(averageTime))
