import pytest
from src.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    raiz_cuadrada,
    promedio,
    maximo,
    minimo,
    calcular_area_rectangulo,
    calcular_perimetro_rectangulo,
)


def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_sumar_negativos():
    # Arrange
    a, b = -3, -2
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == -5
 
 
def test_restar_resultado_negativo():
    # Arrange
    a, b = 3, 10
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -7
 
 
def test_multiplicar_por_cero():
    # Arrange
    a, b = 25, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0
 
 
def test_dividir_numeros_positivos():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 2.5


def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act + Assert
    with pytest.raises(ValueError):
        dividir(a, b)

def test_potencia_exponente_cero():
    # Arrange
    base, exponente = 8, 0
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 1

def test_raiz_cuadrada_numero_positivo():
    # Arrange
    numero = 9
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 3

def test_raiz_cuadrada_de_cero():
    # Arrange
    numero = 0
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 0


def test_raiz_cuadrada_negativo_lanza_error():
    # Arrange
    numero = -4
    # Act + Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)

def test_promedio_lista_normal():
    # Arrange
    numeros = [2, 4, 6]
    # Act
    resultado = promedio(numeros)
    # Assert
    assert resultado == 4
 
 
def test_promedio_lista_vacia_lanza_error():
    # Arrange
    numeros = []
    # Act + Assert
    with pytest.raises(ValueError):
        promedio(numeros)
 
 
def test_maximo_lista_con_negativos():
    # Arrange
    numeros = [-7, -2, -9]
    # Act
    resultado = maximo(numeros)
    # Assert
    assert resultado == -2
 
 
def test_maximo_lista_vacia_lanza_error():
    # Arrange
    numeros = []
    # Act + Assert
    with pytest.raises(ValueError):
        maximo(numeros)
 
 
def test_minimo_lista_solo_positivos():
    numeros = [5, 8, 3]
    # Act
    resultado = minimo(numeros)
    # Assert
    assert resultado == 3
 
 
def test_minimo_lista_con_negativos():
    # Arrange
    numeros = [4, -1, 7]
    # Act
    resultado = minimo(numeros)
    # Assert
    assert resultado == -1
 
 
def test_minimo_lista_vacia_lanza_error():
    # Arrange
    numeros = []
    # Act + Assert
    with pytest.raises(ValueError):
        minimo(numeros)
 
def test_area_rectangulo_normal():
    # Arrange
    base, altura = 4, 5
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 20
 
 
def test_area_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = -4, 5
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)
 
 
def test_perimetro_rectangulo_normal():
    # Arrange
    base, altura = 4, 5
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 18
 
 
def test_perimetro_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = 4, -5
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)
 