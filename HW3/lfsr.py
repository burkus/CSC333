from random import *
from operator import mul,xor
from itertools import starmap
from functools import reduce

#Registers and program are stored in reverse order
#so r[0] is the rightmost register bit

class LFSR(object):

    def __init__(self, p = [1,0,1], r = [0,0,0]):
        'initialize LFSR'
        if len(p) < 1:
            raise ValueError('LFSR needs at least one register')
        self._n = len(p)        #number of registers
        self._p = p             #program
        if len(r) != len(p):
            raise ValueError('Number of registers and program must agree')
        self._r = r             #initial content of registers

    def __repr__(self):
        return 'LFSR({}, {})'.format(self._p, self._r)

    def seed(self, r):
        'seed registers'

        if len(r) != self._n:
            raise ValueError('Number of registers and program must agree')

    def update(self, bit):
        'update register with new bit'

        self._r.append(bit)
        self._r = self._r[1:]

    def run(self):
        'run one iteration of LFSR'

        outbit = self._r[0]
        newbit = 0
        for i in range(self._n):
            newbit = newbit ^ (self._p[i] * self._r[i])
        self.update(newbit)
        return outbit

    #same using some higher-order programming tools
    def run(self):
        'run one interation of LFSR'

        newbit = reduce(xor, starmap(mul, zip(self._p, self._r)))
        outbit = self._r[0]
        self.update(newbit)
        return outbit

    def cur(self):
        'display current state of registers'
        return ''.join(map(str, self._r[::-1])) #or use loop; displaying reg


#R1 implements s_{n+3} = s_{n+1} + s_n
    #namely    s_{n+3} = 0*s_{n+2} + 1*s_{n+1} + 1*s_n
R1 = LFSR([1,1,0],[1,0,0])

#R2 implements s_{n+4} = s_{n+3} + s_n
    #namely    s_{n+3} = 1(s_{n+3} + 0*s_{n+2} + 0*s_{n+1} + 1*s_n
R2 = LFSR([1,0,0,1], [0,0,0,1])

#R3 implements s_{n+3} = s_{n+2} + s_{n+1}
    #namely    s_{n+3} = 1*s_{n+2} + 1*s_{n+1} + 0*s_n
R3 = LFSR([0,1,1],[0,1,0])

#R4 implements s_{n+4} = s_{n+2} + s_{n+1} + s_n
    #namely    s_{n+4} = 0* s_{n+3} + 1*s_{n+2} + 1*s_{n+1} + 1*s_n
R4 = LFSR([1,1,1,0],[1,1,0,1])

#R5 implements s_{n+4} = s_{n+1} + s_n
    #namely    s_{n+4} = 0* s_{n+3} + 0*s_{n+2} + 1*s_{n+1} + 1*s_n
R5 = LFSR([1,1,0,0],[0,1,1,0])

## My Code
R6 = LFSR([0, 1, 0, 1], [0, 0, 0, 1])

R7 = LFSR([1, 1, 0, 0], [1, 1, 1, 0])

#sample run
R = R7

out = ''
for i in range(20):
    reg = R.cur()
    outb = R.run()
    out += str(outb)
    print('Register: {}  Output: {}'.format(reg,outb))
print(out)
