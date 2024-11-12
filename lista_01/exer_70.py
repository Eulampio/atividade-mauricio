
def classifica_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def test_classifica_triangulo():
    assert classifica_triangulo(3, 3, 3) == "Equilátero"
    assert classifica_triangulo(3, 3, 4) == "Isósceles"
    assert classifica_triangulo(3, 4, 5) == "Escaleno"
    print("test_classifica_triangulo passou!")