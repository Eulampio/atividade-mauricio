
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def test_fibonacci_gen():
    assert list(fibonacci_gen(5)) == [0, 1, 1, 2, 3]
    assert list(fibonacci_gen(3)) == [0, 1, 1]
    assert list(fibonacci_gen(1)) == [0]
    print("test_fibonacci_gen passou!")