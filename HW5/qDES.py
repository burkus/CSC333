from time import clock

#Sboxes (the first 2 Sboxes from DES)
Sdata = [[[ 14, 4 , 13, 1 , 2 , 15 , 11 , 8 , 3 , 10 , 6 , 12 , 5 , 9 , 0 , 7],
[0 , 15 , 7 , 4 , 14 , 2 , 13 , 1 , 10 , 6 , 12 , 11 , 9 , 5 , 3 , 8],
[4 , 1 , 14 , 8 , 13 , 6 , 2 , 11 , 15 , 12 , 9 , 7 , 3 , 10 , 5 , 0],
[15 , 12 , 8 , 2 , 4 , 9 , 1 , 7 , 5 , 11 , 3 , 14 , 10 , 0 , 6 , 13]] ,

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]] ]

#Expansion function spec: 1st bit of output is 16th bit of input, 2nd bit is first, etc.
Elst = [8, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 1]

#calculate S-box
def S(k,x):
    x = x & 0x3F  #(keep 6 bits)
    row = ((x>>5)<<1) + (x&1)
    col = (x>>1)& 0xF
    #print(row, col)
    return Sdata[k-1][row][col]

#calculate round key (12 bits) for ith round of simplified DES
def roundkey(k,i):
    #rotate key by i positions, and then take 12 bits
    return (((k<<16)+k)>>i) & 0xFFF

#expand 8bits to 12 bits
def E(x):
    n = len(Elst) # should be 12
    return sum( [((x>>(8-Elst[i]))&1)<<(n-i)   for i in range(n)])

#calculate f for quarter DES on input x, with round key rk
def f(x,rk):
    f1 = E(x)
    f2 = f1^rk
    inp = [0,0] #inputs to S-boxes
    oup = [0,0] #output of S-boxes
    out = 0
    for i in range(1,-1,-1):
        inp[i] = f2 & 0x3F #get last 6 bits
        out = out << 4
        oup[i] = S(i,inp[i])
        out = out + oup[i]
        f2 = f2>>6
    return out

#calculate one round of quarter DES on input x, with round key rk
def round(x,rk):
    Lx = x >> 8 #left quarter of x
    Rx = x & 0xFF #right quarter of x

    return (Rx<<8) + (Lx ^ f(Rx,rk))

#quarter DES encryption: input 16-bit plaintext x, and 16-bit key k
def qtE(x,k):
    x = x & 0xFFFF #restrict to 16 bit blocks
    k = k & 0xFFFF #and 16 bit keys
    for i in range(6):
        x = round(x,roundkey(k,i))
    return ((x & 0xFF)<<8) + (x>>8)

#quarter DES decryption: input 16-bit plaintext x, and 16-bit key k
def qtD(x,k):
    x = x & 0xFFFF #restrict to 16 bit blocks
    k = k & 0xFFFF #and 16 bit keys
    for i in range(6):
        x = round(x,roundkey(k,5-i))
    return ((x & 0xFF)<<8) + (x>>8)

#improved quarter DES encryption with (bad) key whitening
def impqtE(x,k1, k2):
    return qtE(x,k1) ^ k2

#improved quarter DES decryption with (bad) key whitening
def impqtD(x,k1,k2):
    return qtD(x^k2,k1)
