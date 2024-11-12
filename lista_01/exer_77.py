
def le_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return f.read()


def test_le_arquivo():
    le_arquivo('arquivo_teste.txt', 'Conteúdo do arquivo')
    assert le_arquivo('arquivo_teste.txt') == 'Conteúdo do arquivo'
    print("test_le_arquivo passou!")