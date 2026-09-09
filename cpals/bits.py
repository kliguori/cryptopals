def hamming(a: bytes, b: bytes) -> int:
    if len(a) != len(b):
        raise ValueError("Must be the same number of bytes")
    return sum((x ^ y).bit_count() for x, y in zip(a, b))
