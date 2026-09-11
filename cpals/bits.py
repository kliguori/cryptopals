def hamming(a: bytes, b: bytes) -> int:
    if len(a) != len(b):
        raise ValueError("Must be the same number of bytes")
    return sum((x ^ y).bit_count() for x, y in zip(a, b))


def chunking(data: bytes, size: int, num_chunks: int | None = None) -> list[bytes]:
    # Check for sane inputs
    if size <= 0:
        raise ValueError("size must be a positive integer")
    if num_chunks is not None and num_chunks <= 0:
        raise ValueError("num_chunks must be a positive integer or None")

    n = len(data)
    available_chunks = n // size + int(n % size != 0)

    if num_chunks is None:
        num_chunks = available_chunks
    elif num_chunks > available_chunks:
        raise ValueError("num_chunks exceeds number of available chunks")

    return [data[size * i : size * (i + 1)] for i in range(num_chunks)]


def transposed_chunking(data: bytes, size: int) -> list[bytes]:
    return [data[i::size] for i in range(size)]
