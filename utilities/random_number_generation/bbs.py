from primes import GeneratePrimes

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
    psize = bits // 2
    f = lambda x : GeneratePrimes.getStrongBlumPrime(x)
    return f(psize) * f(psize)


class BBS:
    def __init__(self, seed, bits=2048):
        self.mod = getModulus(bits)
        self.seq = seed
    
    def seed(self, seed):
        self.seq = seed

    def gen(self, bits):
        out = int(0)

        for _ in range(0, bits):
            self.seq = pow(self.seq, 2, self.mod)
            lsb = int(bin(self.seq)[-1])
            out = (out << 1) + lsb

        return out
