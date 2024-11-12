
def dec2bin(n):
    return bin(n)[2:]

def test_dec2bin():
    assert dec2bin(10) == "1010"
    assert dec2bin(0) == "0"
    assert dec2bin(255) == "11111111"
    print("test_dec2bin passou!")