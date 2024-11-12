
def substitui_texto_arquivo(nome_arquivo, palavra_antiga, palavra_nova):
    with open(nome_arquivo, 'r') as f:
        conteudo = f.read()
    conteudo = conteudo.replace(palavra_antiga, palavra_nova)
    with open(nome_arquivo, 'w') as f:
        f.write(conteudo)

def test_substitui_texto_arquivo():
    test_substitui_texto_arquivo('arquivo_substitui.txt', 'Eu gosto de maçã.')
    substitui_texto_arquivo('arquivo_substitui.txt', 'maçã', 'banana')
    assert test_substitui_texto_arquivo('arquivo_substitui.txt') == 'Eu gosto de banana.'
    print("test_substitui_texto_arquivo pas")