from Crypto.Util import number

"""
    A file to help generate various types
    of prime numbers
"""

def gcd(a, b):
    while not b == 0:
        t = b
        b = a % b
        a = t
    return a

class CheckPrimes:
    def isPrime(p):
        return number.isPrime()
        
    def isStrongPrime(p):
        nextp = p + 1
        while not number.isPrime(nextp):
            nextp = nextp + 1

        lastp = p - 1
        while not number.isPrime(lastp):
            lastp = lastp - 1

        return (p * 2 > nextp + lastp)

    def isBlumPrime(p):
        return (p % 4) == 3

    def isStrongBlumPrime(p):
        return (CheckPrimes.isBlumPrime(p) and CheckPrimes.isStrongPrime(p))

    def areCoPrime(p, q):
        return (gcd(p, q) == 1)


class GeneratePrimes:
    def getPrime(bits=1024, cond=lambda _ : True):
        while True:
            p = number.getPrime(bits)
            if cond(p):
                return p

    def getStrongPrime(bits=1024):
        return GeneratePrimes.getPrime(bits, CheckPrimes.isStrongPrime)

    def getBlumPrime(bits=1024):
        return GeneratePrimes.getPrime(bits, CheckPrimes.isBlumPrime)

    def getStrongBlumPrime(bits=1024):
        return GeneratePrimes.getPrime(bits, CheckPrimes.isStrongBlumPrime)
