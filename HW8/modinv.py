
def inv(a,n):
    'calculate inverse of a modulo n'
    error = '{} is not invertible mod {}'.format(a,n)
    a = a % n
    a, b = n, a
    y0, y1 = 0, 1
    while (b > 0):
        q = a // b
        a, b = b, a - q*b
        y0, y1 = y1, y0 - q*y1
    y0 = y0 % n
    if a > 1:
        raise ValueError(error)
    return y0  
