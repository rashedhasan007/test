import pyspx.shake256_128f as sphincs
import os, binascii

# Key generation: private + public key
seed = os.urandom(sphincs.crypto_sign_SEEDBYTES)
public_key, secret_key = sphincs.generate_keypair(seed)
print("Public key:", binascii.hexlify(public_key))
print("Private key:", binascii.hexlify(secret_key))

# Sign message and verify signature
message = b'Message for SPHINCS+ shake256_128f signing'
signature = sphincs.sign(message, '6b6ca378b9c38e0db41a215ab6d43b62d6fd78bdf244e581a2c1ff5b97bda6e9')
valid = sphincs.verify(message, signature,'0x27375f11eBE6d49edbD64bE6D9E9c2CeE077Ab75')


# Verify tampered message + signature
message = b'Tampered msg'
valid = sphincs.verify(message, signature, public_key)
print("Tampered signature valid?", valid)
