
import re

def valida_email(email):
    padrao = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(padrao, email))

# Teste para a função valida_email
def test_valida_email():
    assert valida_email("teste@exemplo.com") == True
    assert valida_email("testeexemplo.com") == False
    assert valida_email("test@com") == False
    print("test_valida_email passou!")