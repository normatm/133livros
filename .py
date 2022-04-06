import pytest

import main

lista_para_multiplicar =
        (2, 3, 6),
        (0, 4, 0)
        (-5, -3, 15)
        (8, 1000, 8000)

@pytest.mark.parametrize('numero1, numero2, resultado_esperado')
def test_multiplicar_2_numeros(numero1, numero2, resultado_esperado):
    # Configura - virá da lista

    # Executa
    resultado_obtido = main.multiplicar_2_numeros (numero1, numero2)

    # Valida
    assert resultado_esperado == resultado_obtido


