FREQ = {
    "a": 0.082,
    "b": 0.015,
    "c": 0.028,
    "d": 0.043,
    "e": 0.127,
    "f": 0.022,
    "g": 0.020,
    "h": 0.061,
    "i": 0.070,
    "j": 0.0016,
    "k": 0.0077,
    "l": 0.040,
    "m": 0.024,
    "n": 0.067,
    "o": 0.075,
    "p": 0.019,
    "q": 0.0012,
    "r": 0.060,
    "s": 0.063,
    "t": 0.091,
    "u": 0.028,
    "v": 0.0098,
    "w": 0.024,
    "x": 0.0015,
    "y": 0.020,
    "z": 0.00074,
}


def score(s):
    count = {}
    n = len(s)
    for c in s:
        count[c] = count.get(c, 0) + 1
    frequencies = {c: i / n for c, i in count.items()}
    return sum((f - frequencies.get(k, 0)) ** 2 for k, f in FREQ.items()) ** 0.5
