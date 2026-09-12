from cpals.bits import chunking

f = open("data/c08.txt")

for lineno, line in enumerate(f, start=1):
    chunks = chunking(bytes.fromhex(line), 16)
    test_dict = {}
    for chunk in chunks:
        test_dict[chunk] = test_dict.get(chunk, 0) + 1
    if max(test_dict.values()) > 1:
        print(lineno, "::", line)
