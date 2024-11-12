
def pares(n):
    for i in range(2, n + 1, 2):
        yield i

def test_pares():
    assert list(pares(10)) == [2, 4, 6, 8, 10]
    assert list(pares(5)) == [2, 4]
    assert list(pares(2)) == [2]
    print("test_pares passou!")