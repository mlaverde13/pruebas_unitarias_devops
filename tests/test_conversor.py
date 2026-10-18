import pytest
from src.conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    metros_a_kilometros,
    kilometros_a_metros,
    libras_a_kilogramos,
    kilogramos_a_libras,
    galones_a_litros,
    litros_a_galones,
    millas_a_kilometros,
    kilometros_a_millas,
    pies_a_metros,
    metros_a_pies,
    onzas_a_gramos,
    gramos_a_onzas,
)



def test_celsius_a_fahrenheit_punto_ebullicion():
    # Arrange
    celsius = 100
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 212


def test_celsius_a_fahrenheit_menos_40_coinciden():
    # Arrange  (único punto donde ambas escalas son iguales)
    celsius = -40
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == -40


def test_fahrenheit_a_celsius_punto_congelacion():
    # Arrange
    fahrenheit = 32
    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)
    # Assert
    assert resultado == 0


def test_celsius_a_kelvin_cero():
    # Arrange
    celsius = 0
    # Act
    resultado = celsius_a_kelvin(celsius)
    # Assert
    assert resultado == pytest.approx(273.15)


def test_kelvin_a_celsius_normal():
    # Arrange
    kelvin = 273.15
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(0)


def test_kelvin_a_celsius_cero_absoluto():
    # Arrange  (límite: 0 K sí es válido)
    kelvin = 0
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(-273.15)


def test_kelvin_negativo_lanza_error():
    # Arrange  (revela el BUG 1: no existe temperatura bajo el cero absoluto)
    kelvin = -10
    # Act + Assert
    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)



def test_metros_a_kilometros():
    # Arrange
    metros = 2500
    # Act
    resultado = metros_a_kilometros(metros)
    # Assert
    assert resultado == 2.5


def test_kilometros_a_metros():
    # Arrange
    kilometros = 3
    # Act
    resultado = kilometros_a_metros(kilometros)
    # Assert
    assert resultado == 3000


def test_millas_a_kilometros():
    # Arrange
    millas = 1
    # Act
    resultado = millas_a_kilometros(millas)
    # Assert
    assert resultado == pytest.approx(1.60934)


def test_kilometros_a_millas():
    # Arrange  (revela el BUG 2: 1.60934 km deben ser 1 milla)
    kilometros = 1.60934
    # Act
    resultado = kilometros_a_millas(kilometros)
    # Assert
    assert resultado == pytest.approx(1)


def test_pies_a_metros():
    # Arrange
    pies = 10
    # Act
    resultado = pies_a_metros(pies)
    # Assert
    assert resultado == pytest.approx(3.048)


def test_metros_a_pies():
    # Arrange
    metros = 3.048
    # Act
    resultado = metros_a_pies(metros)
    # Assert
    assert resultado == pytest.approx(10)




def test_libras_a_kilogramos():
    # Arrange
    libras = 1
    # Act
    resultado = libras_a_kilogramos(libras)
    # Assert
    assert resultado == pytest.approx(0.453592)


def test_kilogramos_a_libras():
    # Arrange
    kilogramos = 0.453592
    # Act
    resultado = kilogramos_a_libras(kilogramos)
    # Assert
    assert resultado == pytest.approx(1)


def test_onzas_a_gramos():
    # Arrange
    onzas = 2
    # Act
    resultado = onzas_a_gramos(onzas)
    # Assert
    assert resultado == pytest.approx(56.699)


def test_gramos_a_onzas():
    # Arrange
    gramos = 28.3495
    # Act
    resultado = gramos_a_onzas(gramos)
    # Assert
    assert resultado == pytest.approx(1)


def test_galones_a_litros():
    # Arrange
    galones = 1
    # Act
    resultado = galones_a_litros(galones)
    # Assert
    assert resultado == pytest.approx(3.78541)


def test_litros_a_galones():
    # Arrange
    litros = 3.78541
    # Act
    resultado = litros_a_galones(litros)
    # Assert
    assert resultado == pytest.approx(1)




@pytest.mark.parametrize("funcion", [
    metros_a_kilometros,
    kilometros_a_metros,
    libras_a_kilogramos,
    kilogramos_a_libras,
    galones_a_litros,
    litros_a_galones,
    millas_a_kilometros,
    kilometros_a_millas,
    pies_a_metros,
    metros_a_pies,
    onzas_a_gramos,
    gramos_a_onzas,
])
def test_valor_negativo_lanza_error(funcion):
    # Arrange
    valor_negativo = -1
    # Act + Assert
    with pytest.raises(ValueError):
        funcion(valor_negativo)