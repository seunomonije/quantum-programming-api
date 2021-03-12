import qapi
from qapi.src.protocols.cryptography.key_distribution.KeyGenerator import KeyGenerator

generator = KeyGenerator()
generator.generate()
generator.print_keys()