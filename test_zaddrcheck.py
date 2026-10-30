from zaddrcheck import validate_address

def test_transparent():
    res = validate_address("t14G2S9A2A1e23345678901234567890123")
    assert res["valid"] is True
    assert res["type"] == "transparent"

def test_sapling():
    res = validate_address("zs1z7rejlps4hs3228tfw2x6cca4hcc2702bd0e35ac23y32q52345678901234567890123456789")
    assert res["valid"] is True
    assert res["type"] == "sapling"

def test_empty_input():
    res = validate_address("")
    assert res["valid"] is False
    assert res["type"] == "invalid"

def test_malformed_input():
    res = validate_address("invalid_address_string")
    assert res["valid"] is False
    assert res["type"] == "invalid"