from primes import GeneratePrimes, CheckPrimes

"""
    An implementation of the Blum Blum Shub pseduo-random 
    number generator.
    
    General Notes:
        - BBS must be initialized with a random seed
        - In order for BBS to produce cryptographically secure
          output, the seed must be truly random
        - In order for the generator to be practically secure, the 
          bit length of the modulus should be no less than 2048
        - The functions used to generate the modulus of the
          function rely on PyCryptodome's Crypto.Util package
"""

"""
    Returns an integer n = p * q where p and q are primes of the
    form needed for BBS.
"""
def getModulus(bits=2048):
    f = lambda x : GeneratePrimes.getStrongBlumPrime(x)
    psize = bits // 2

    p = f(psize)
    q = f(psize)

    while p == q:       # Ensures p does not equal q
        q = f(psize)

    return p * q


class BBS:
    def __init__(self, seed, bits=2048):
        self.seq = seed
        while True:     # Ensures the seed and modulus are coprime                            
            self.mod = getModulus(bits)
            if CheckPrimes.areCoPrime(seed, self.mod):
                break
    
    def seed(self, seed):
        self.seq = seed

    def getNum(self, bits):
        out = int(0)

        for _ in range(0, bits):
            self.seq = pow(self.seq, 2, self.mod)
            lsb = int(bin(self.seq)[-1])
            out = (out << 1) + lsb

        return out
