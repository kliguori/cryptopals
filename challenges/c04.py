from cpals.convert import from_hex, to_hex
from cpals.english import english_score
from cpals.xor import xor

current_score = -100_000
current_plaintext = b""
current_key = ""
current_line = 0

with open("data/c04.txt") as f:
    for lineno, line in enumerate(f, start=1):
        line = line.strip()
        cyphertext_bytes = from_hex(line)
        for i in range(256):
            key = i.to_bytes(1)
            plaintext_bytes = xor(cyphertext_bytes, key)
            plaintext_score = english_score(plaintext_bytes)
            if plaintext_score > current_score:
                current_score = plaintext_score
                current_plaintext = plaintext_bytes
                current_key = key
                current_line = lineno

print(
    current_line,
    "::",
    current_score,
    "::",
    to_hex(current_key),
    "::",
    current_plaintext.decode("utf-8"),
)
