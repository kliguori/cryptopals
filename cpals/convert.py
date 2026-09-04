import string

# --- Hex ---
HEXCHARS = "0123456789abcdef"
HEXVALS = {c: i for i, c in enumerate(HEXCHARS)}


def to_hex(b):
    out = []
    for byte in b:
        i1, i2 = byte // 16, byte % 16
        out.append(HEXCHARS[i1])
        out.append(HEXCHARS[i2])
    return "".join(out)


def from_hex(s):
    out = []
    s = s.strip().lower()
    num_chars = len(s)
    if num_chars % 2:
        raise ValueError("hex string must have even length")
    for i in range(0, num_chars, 2):
        p1, p2 = s[i], s[i + 1]
        if p1 not in HEXVALS or p2 not in HEXVALS:
            raise ValueError(p1, p2, " is not a valid hex pair")
        out.append(16 * HEXVALS[p1] + HEXVALS[p2])
    return bytes(out)


# --- Base64 ---
B64CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
B64VALS = {c: i for i, c in enumerate(B64CHARS)}


def to_b64(b):
    out = []
    for i in range(0, len(b), 3):
        group = b[i : i + 3]
        if len(group) == 3:
            chunk = (
                group[0] << 16 | group[1] << 8 | group[2]
            ) << 0  # no bit padding 4 b64 chars
            shifts, pad = (18, 12, 6, 0), ""
        elif len(group) == 2:
            chunk = (
                group[0] << 8 | group[1]
            ) << 2  # pad with 2 zeros to get 3 b64 chars
            shifts, pad = (12, 6, 0), "="
        else:
            chunk = group[0] << 4  # pad with 4 zeros to get 2 b64 chars
            shifts, pad = (6, 0), "=="
        out.extend(B64CHARS[(chunk >> shift) & 0b111111] for shift in shifts)
        out.append(pad)
    return "".join(out)


def from_b64(s):
    pass
