
def ordena_por_valores(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1]))

def test_ordena_por_valores():
    assert ordena_por_valores({'a': 3, 'b': 1, 'c': 2}) == {'b': 1, 'c': 2, 'a': 3}
    assert ordena_por_valores({'x': 5, 'y': 2, 'z': 4}) == {'y': 2, 'z': 4, 'x': 5}
    assert ordena_por_valores({'a': 1}) == {'a': 1}
    print("test_ordena_por_valores passou!")