#! python3
from modinv import inv
from week7a import modexp
from fractions import gcd
from random import randrange

e, n = 318418963, 1768912591195703556689
phiN = 1768912591108490108400
ct = 863673585627860652544
d = inv(e, phiN)
message = modexp(ct, d, n)

def pollard0(a, n, B):
    pairs = []
    for i in range(2, B + 1):
        a = modexp(a, i, n)
        d = gcd(a - 1, n)
        if d > 1 and d < n:
            pair = (d, n //d)
            if pair not in pairs:
                pairs.append(pair)
                print('(p, q) =', pair)
    return pairs

def pollard1(n, B=10000000):
    a = randrange(1, n)
    return pollard0(a, n, B)

def padbreak():
    e, n = (4063890433427654625912531070549716807, 1623441316873935161434058866871742468397)
    map = {}
    for i in range(97, 122 + 1):
        power = 1
        base = i
        while base < n:
            base = base * (10 ** power)
            encrypt = modexp(base, e, n)
            map[encrypt] = i

    return map

def breakAliceandBob():
    messages = [416707656951420132306740205974514891672, 767698358188094347735042830286015455666, 333401982569588859849838422320396925912, 1122509848831388788012513600518758986823, 911503646795964084274775328404658566844, 638437764491916645468397088077059577779]

    map = padbreak()
    originalMessage = ''
    for message in messages:
        character = chr(map[message])
        originalMessage += character
        print(originalMessage)
