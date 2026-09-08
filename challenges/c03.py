import string
from cpals.convert import from_hex
from cpals.english import english_score

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
cyphertext_bytes = from_hex(s)
n_bytes = len(cyphertext_bytes)

out = {}

for ch in string.ascii_lowercase + string.ascii_uppercase:
    key = ch.encode("ascii") * n_bytes  # key in bytes padded to match cyphertext_bytes
    plaintext_bytes = bytes(key[i] ^ cyphertext_bytes[i] for i in range(n_bytes))
    plaintext = plaintext_bytes.decode("ascii")
    plaintext_score = english_score(plaintext_bytes)
    out[ch] = [plaintext, plaintext_score]

results = dict(sorted(out.items(), key=lambda kv: kv[1][-1], reverse=True))
for i in range(len(results)):
    v = list(results.items())
    print(v[i][1][1], "::", v[i][0], "::", repr(v[i][1][0]))
