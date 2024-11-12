
def escreve_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w') as f:
        f.write(texto)

def test_escreve_arquivo():
    escreve_arquivo('arquivo_teste.txt', 'Olá, Mundo!')
    with open('arquivo_teste.txt', 'r') as f:
        assert f.read() == 'Olá, Mundo!'
    print("test_escreve_arquivo passou!")