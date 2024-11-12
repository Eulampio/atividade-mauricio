
def conta_palavras_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return len(f.read().split())

def test_conta_palavras_arquivo():
    conta_palavras_arquivo('arquivo_palavras.txt', 'Este é um arquivo com várias palavras.')
    assert conta_palavras_arquivo('arquivo_palavras.txt') == 7
    print("test_conta_palavras_arquivo passou!")