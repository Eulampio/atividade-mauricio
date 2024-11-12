
def conta_ate_n(n):
    for i in range(1, n + 1):
        yield i

# Teste para a função conta_ate_n
def test_conta_ate_n():
    assert list(conta_ate_n(5)) == [1, 2, 3, 4, 5]
    assert list(conta_ate_n(3)) == [1, 2, 3]
    assert list(conta_ate_n(1)) == [1]
    print("test_conta_ate_n passou!")