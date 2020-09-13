import pyspx.shake256_128f as sphincs
import os, binascii

# Key generation: private + public key
seed = os.urandom(sphincs.crypto_sign_SEEDBYTES)
public_key, secret_key = sphincs.generate_keypair(seed)
print("Public key:", binascii.hexlify(public_key))
print("Private key:", binascii.hexlify(secret_key))

# Sign message and verify signature
message = b'Message for SPHINCS+ shake256_128f signing'
signature = sphincs.sign(message, secret_key)
valid = sphincs.verify(message, signature, public_key)


# Verify tampered message + signature
message = b'Tampered msg'
valid = sphincs.verify(message, signature, public_key)
print("Tampered signature valid?", valid)
