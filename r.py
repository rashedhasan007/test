import pyspx.shake256_128f
import pyspx.shake256_128f as sphincs
import os, binascii
message = b'Message for SPHINCS+ shake256_128f signing'
seed = os.urandom(sphincs.crypto_sign_SEEDBYTES)
public_key, secret_key = pyspx.shake256_128f.generate_keypair(seed)
signature = pyspx.shake256_128f.sign(message, secret_key)
print(signature)
print(public_key)
