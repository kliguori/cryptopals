import operator
from itertools import cycle
from cpals.convert import to_hex, from_hex


def fixed_xor(s1, s2):
    out = []
    if len(s1) != len(s2):
        raise ValueError("The buffers must be the same size")
    b1, b2 = from_hex(s1), from_hex(s2)
    for i in range(len(b1)):
        out.append(b1[i] ^ b2[i])
    return to_hex(out)


def xor(data: bytes, key: bytes) -> bytes:
    return bytes(map(operator.xor, data, cycle(key)))
