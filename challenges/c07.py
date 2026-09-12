from base64 import b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

f = open("data/c07.txt")
contents = "".join(f.read().split())
ct = b64decode(contents)

key = b"YELLOW SUBMARINE"
cipher = Cipher(algorithms.AES(key), modes.ECB())
dec = cipher.decryptor()
pt = dec.update(ct) + dec.finalize()

print(pt.decode("utf-8"))
