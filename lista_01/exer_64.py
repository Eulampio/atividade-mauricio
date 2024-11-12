
import random
import string

def gera_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def test_gera_senha():
    senha = gera_senha(10)
    assert len(senha) == 10
    assert any(c.isdigit() for c in senha)
    assert any(c.isupper() for c in senha)
    print("test_gera_senha passou!")