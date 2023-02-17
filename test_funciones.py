from funciones import sumar, es_primo


def test_sumar():
    assert sumar(2,4) == 6
    assert sumar(-2,2) == 0
    assert sumar(2,2) == 5
    
def test_es_primo():
    assert es_primo(7) is True
    assert es_primo(4) is False