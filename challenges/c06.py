from cpals.attacks import crack_repeated_key_xor
from base64 import b64decode


f = open("data/c06.txt")
text = "".join(f.read().split())
cyphertext = b64decode(text)
plaintext = crack_repeated_key_xor(cyphertext, 6)
print(plaintext.decode("utf-8"))
