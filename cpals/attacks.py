from cpals.bits import hamming


def crack_repeated_key_xor(data: bytes, num_chunks: int = 2) -> bytes:
    key_size_dict = {}
    for keysize in range(2, 41):
        chunk_rng = range(num_chunks)
        chunks = [data[keysize * i : keysize * (i + 1)] for i in chunk_rng]
        hamming_distances = []
        for i in chunk_rng:
            for j in range(i + 1, num_chunks):
                hamming_distances.append(hamming(chunks[i], chunks[j]))
        avg_hamming = sum(hamming_distances) / len(hamming_distances)
        key_size_dict[keysize] = round(avg_hamming / keysize, 3)
    key_size_dict_sorted = dict(sorted(key_size_dict.items(), key=lambda kv: kv[1]))

    for i in range(5):
        pass

    return b"00"
