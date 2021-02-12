from Crypto.Util import number

"""
    A file to help generate various types
    of prime numbers
"""

def isStrongPrime(p):
    if not number.isPrime(p):
        return False

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
    return (isBlumPrime(p) and isStrongPrime(p))

def getPrime(bits=1024, cond=lambda _ : True):
    while True:
        p = number.getPrime(bits)
        if cond(p):
            return p


def getStrongPrime(bits=1024):
    return getPrime(bits, isStrongPrime)

def getBlumPrime(bits=1024):
    return getPrime(bits, isBlumPrime)

def getStrongBlumPrime(bits=1024):
    return getPrime(bits, isStrongBlumPrime)

