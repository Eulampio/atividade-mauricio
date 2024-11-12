
def conta_linhas(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return len(f.readlines())


def test_conta_linhas():
    conta_linhas('arquivo_linhas.txt', 'Linha 1\nLinha 2\nLinha 3\n')
    assert conta_linhas('arquivo_linhas.txt') == 3
    print("test_conta_linhas passou!")