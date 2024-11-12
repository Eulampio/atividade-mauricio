
def filtro_dicionario(dic, valor):
    return {k: v for k, v in dic.items() if v > valor}

def test_filtro_dicionario():
    assert filtro_dicionario({'a': 1, 'b': 3, 'c': 2}, 2) == {'b': 3}
    assert filtro_dicionario({'x': 5, 'y': 1, 'z': 4}, 3) == {'x': 5, 'z': 4}
    assert filtro_dicionario({'a': 1, 'b': 1}, 1) == {}
    print("test_filtro_dicionario passou!")