
def quadrados(n):
    for i in range(1, n + 1):
        yield i ** 2

def test_quadrados():
    assert list(quadrados(5)) == [1, 4, 9, 16, 25]
    assert list(quadrados(3)) == [1, 4, 9]
    assert list(quadrados(1)) == [1]
    print("test_quadrados passou!")