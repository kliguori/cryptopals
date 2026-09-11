from cpals.bits import hamming, chunking


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


def crack_repeated_key_xor(
    data: bytes, num_chunks: int = 2, num_sizes: int = 4
) -> bytes:
    keysizes = list(get_key_sizes(data, num_chunks))[:num_sizes]

    for keysize in keysizes:
        pass

    return b"00"
