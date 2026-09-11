from cpals.xor import xor
from cpals.english import english_score
from cpals.bits import hamming, chunking, transposed_chunking


def get_key_sizes(data: bytes, num_chunks: int = 2) -> dict[int, float]:
    key_size_dict = {}
    for keysize in range(2, 41):
        chunks = chunking(data, keysize, num_chunks)
        hamming_distances = []
        for i in range(num_chunks):
            for j in range(i + 1, num_chunks):
                hamming_distances.append(hamming(chunks[i], chunks[j]))
        avg_hamming = sum(hamming_distances) / len(hamming_distances)
        key_size_dict[keysize] = round(avg_hamming / keysize, 2)
    return dict(sorted(key_size_dict.items(), key=lambda kv: kv[1]))


def find_key(data: bytes) -> bytes:
    current_score = -100_000
    current_key = b""
    for i in range(256):
        key = i.to_bytes(1)
        plaintext_bytes = xor(data, key)
        plaintext_score = english_score(plaintext_bytes)
        if plaintext_score > current_score:
            current_key = key
            current_score = plaintext_score
    return current_key


def crack_repeated_key_xor(data: bytes, num_chunks: int = 2) -> bytes:
    keysizes = list(get_key_sizes(data, num_chunks))[:4]
    keys = {}
    for keysize in keysizes:
        transposed_chunks = transposed_chunking(data, keysize)
        key = []
        for chunk in transposed_chunks:
            key.append(find_key(chunk))
        keys[keysize] = b"".join(key)

    current_score = -100_000
    current_message = b""
    for keysize, key in keys.items():
        plaintext_bytes = xor(data, key)
        plaintext_score = english_score(plaintext_bytes)
        if plaintext_score > current_score:
            current_message = plaintext_bytes
            current_score = plaintext_score

    return current_message
