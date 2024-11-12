
from collections import Counter

def conta_elementos(lista):
    return dict(Counter(lista))

def test_conta_elementos():
    assert conta_elementos([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert conta_elementos(['a', 'b', 'b', 'c', 'c', 'c']) == {'a': 1, 'b': 2, 'c': 3}
    assert conta_elementos([1]) == {1: 1}
    print("test_conta_elementos passou!")