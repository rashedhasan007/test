import pyspx.shake256_128f

public_key, secret_key = pyspx.shake256_128f.generate_keypair(seed)
signature = pyspx.shake256_128f.sign(message, secret_key)
print(signature)
print(publickey)
