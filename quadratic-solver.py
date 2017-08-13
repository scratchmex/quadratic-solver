# Written by Ivan Gonzalez (2017)
from math import sqrt, fmod

def mcd(a, b, *args):
    a, b = abs(a), abs(b)
    if a<b:
        a, b = b, a
    while b:
        a, b = b, fmod(a,b)
    if args:
        return mcd(a, args[0], *args[1:])
    else:
        return a

def solve(a, b=0, c=0):
    q = mcd(a, b, c)
    try:
        x = [(-b+sqrt(b**2-4*(a*c)))/(2*a), (-b-sqrt(b**2-4*(a*c)))/(2*a)]
    except Exception:
        print 'No solutions'
    else:
        print 'For {}(x^2) {:+}(x) {:+}'.format(a, b, c), 'simplified -> {}*[{}(x^2) {:+}(x) {:+}]'.format(q, a/q, b/q, c/q) if q is not 1 else ''
        print 'Solution {}(x{:+})*(x{:+})'.format(str(q)+'*' if q is not 1 else '', -x[0], -x[1])

a = input('a=')
b = input('b=')
c = input('c=')
solve(a,b,c)
