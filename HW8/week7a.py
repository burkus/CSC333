
#assumes that r >= 0 is an integer
def modexp(a,r,m):
    'calculate a**r mod m'

    result = 1
    base = a

    while r > 0:
        if r % 2 == 1:
            result = result * base % m
        base = base * base % m
        r = r//2

    return result

#assumes b >= 0, and a and b are integers

def gcd(a,b):
    'calculate gcd of a and b'

    while b>0:
        a,b = b,a%b
    return a
