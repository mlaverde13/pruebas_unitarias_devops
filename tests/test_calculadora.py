import pytest
from src.calculadora import sumar, dividir, minimo, raiz_cuadrada


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

def test_raiz_cuadrada_numero_positivo():
    # Arrange
    numero = 9
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 3


def test_raiz_cuadrada_negativo_lanza_error():
    # Arrange
    numero = -4
    # Act + Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)