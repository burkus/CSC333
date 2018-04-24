# HW4
# DES Stuff

def getInnerBits(n):
    n >>= 1
    index = 0
    sum = 0
    while index < 4:
        if n & 1 is 1:
            sum += 2 ** index
        index += 1
        n >>= 1
    return sum

def getOuterBits(n):
    firstBit = n & 1
    lastBit = n >> 5
    if firstBit and lastBit:
        return 3
    elif firstBit:
        return 1
    elif lastBit:
        return 2
    else:
        return 0

def binToInt(b):
    integer = 0
    for i, bit in enumerate(b[::-1]):
        if int(bit):
            integer += 2 ** i

    return integer

def s1(i):
    row0 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
    row1 = [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8]
    row2 = [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0]
    row3 = [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    box = [row0, row1, row2, row3]
    row = getOuterBits(i)
    col = getInnerBits(i)
    return box[row][col]

def s3(i):
    row0 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8]
    row1 = [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1]
    row2 = [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7]
    row3 = [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    box = [row0, row1, row2, row3]
    row = getOuterBits(i)
    col = getInnerBits(i)
    return box[row][col]

def dist(a, b):
    difference = a ^ b
    count = 0
    while difference > 0:
        if difference & 1 is 1:
            count += 1
        difference >>= 1
    return count


def testIntegers():
    max = 2 ** 6
    powers = [1, 2, 4, 8, 16, 32]
    for i in range(0, max):
        for j in powers:
            q = i ^ j
            print('x: ' + str(i) + ', ', end='')
            print("x': " + str(q) + ', ', end='')
            print("#diff: " + str(dist(s1(i), s1(q))))
