from cpals import convert


def test_from_hex():
    assert convert.from_hex("4d616e") == b"Man"
    assert convert.to_hex(b"Man") == "4d616e"


def test_to_b64_known():
    assert convert.to_b64(b"Man") == "TWFu"
    assert convert.to_b64(b"Ma") == "TWE="
    assert convert.to_b64(b"M") == "TQ=="
    assert convert.to_b64(b"") == ""
