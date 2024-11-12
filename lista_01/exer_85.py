
from datetime import datetime

def formato_24h_para_12h(hora_24h):
    return datetime.strptime(hora_24h, "%H:%M").strftime("%I:%M %p")

# Teste para a função formato_24h_para_12h
def test_formato_24h_para_12h():
    assert formato_24h_para_12h("14:30") == "02:30 PM"
    assert formato_24h_para_12h("00:00") == "12:00 AM"
    assert formato_24h_para_12h("01:45") == "01:45 AM"
    print("test_formato_24h_para_12h passou!")