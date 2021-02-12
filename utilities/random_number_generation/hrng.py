from os import urandom

"""
    Uses os.urandom() to get a random number generated
    from hardware and OS dependent implementations.
"""

def genNumber(byte_len=8):
    temp = urandom(byte_len)

    out = int(0)
    for x in temp:
        out = (out << 8) + x

    return out

