import string
from cpals.convert import from_hex
from cpals.english import english_score

with open("data/c04.txt") as f:
    out = {}
    for lineno, line in enumerate(f, start=1):
        line = line.strip()
        cyphertext_bytes = from_hex(line)
        n_bytes = len(cyphertext_bytes)
        for byte in range(256):
            key = [byte] * n_bytes
            plaintext_bytes = bytes(
                key[i] ^ cyphertext_bytes[i] for i in range(n_bytes)
            )
            plaintext = plaintext_bytes.decode("ascii")
            plaintext_score = english_score(plaintext_bytes)
            out[lineno] = [plaintext, plaintext_score]

        results = dict(sorted(out.items(), key=lambda kv: kv[1][-1], reverse=True))
        for i in range(len(results)):
            v = list(results.items())
            print(v[i][1][1], "::", v[i][0], "::", repr(v[i][1][0]))
