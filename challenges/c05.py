from cpals.xor import repeating_key_xor

key = "ICE"

with open("data/c05.txt") as f:
    cyphertext = repeating_key_xor(f.read().strip(), key)
    print(cyphertext)
