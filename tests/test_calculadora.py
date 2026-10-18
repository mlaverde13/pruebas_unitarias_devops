import pytest
from src.calculadora import sumar, dividir, minimo


def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12


def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act + Assert
    with pytest.raises(ValueError):
        dividir(a, b)


def test_minimo_lista_solo_positivos():
    # Arrange
    numeros = [5, 8, 3]
    # Act
    resultado = minimo(numeros)
    # Assert
    assert resultado == 3