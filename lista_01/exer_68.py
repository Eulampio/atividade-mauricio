
import os

def tamanho_arquivo(nome_arquivo):
    return os.path.getsize(nome_arquivo)

def test_tamanho_arquivo():
    with open('teste.txt', 'w') as f:
        f.write("Este é um arquivo de teste.")
    assert tamanho_arquivo('teste.txt') == 22
    os.remove('teste.txt')
    print("test_tamanho_arquivo passou!")