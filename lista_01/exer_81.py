
def data_atual():
    return data_atual.now().strftime("%d/%m/%Y")

def test_data_atual():
    assert data_atual() == data_atual.now().strftime("%d/%m/%Y")
    print("test_data_atual passou!")