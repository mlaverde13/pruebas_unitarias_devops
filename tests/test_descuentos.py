import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado,
)


def test_aplicar_descuento_normal():
    # Arrange
    precio, porcentaje = 200, 25
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 150


def test_aplicar_descuento_cero_por_ciento():
    # Arrange  (límite inferior del rango)
    precio, porcentaje = 80, 0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 80


def test_aplicar_descuento_cien_por_ciento():
    # Arrange  (límite superior del rango)
    precio, porcentaje = 80, 100
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0


def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -10, 20
    # Act + Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_porcentaje_mayor_a_100_lanza_error():
    # Arrange
    precio, porcentaje = 100, 101
    # Act + Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)



def test_calcular_descuento_monto():
    # Arrange
    precio, porcentaje = 50, 10
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 5


def test_calcular_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -50, 10
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


def test_calcular_descuento_porcentaje_negativo_lanza_error():
    # Arrange
    precio, porcentaje = 50, -1
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)




def test_precio_final_impuesto_sobre_precio_con_descuento():
    # Arrange  (revela el BUG 1: 100 - 20% = 80; 80 + 10% = 88)
    precio, impuesto, descuento = 100, 10, 20
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(88)


def test_precio_final_sin_impuesto_ni_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 0, 0
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 100


def test_precio_final_precio_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = -100, 10, 20
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


def test_precio_final_impuesto_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, -10, 20
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


def test_precio_final_descuento_fuera_de_rango_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, 10, 150
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)




def test_volumen_menos_de_10_sin_descuento():
    # Arrange
    cantidad, precio_unitario = 9, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 90


def test_volumen_exactamente_10_da_5_por_ciento():
    # Arrange
    cantidad, precio_unitario = 10, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(95)


def test_volumen_exactamente_20_da_10_por_ciento():
    # Arrange
    cantidad, precio_unitario = 20, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(180)


def test_volumen_exactamente_50_da_15_por_ciento():
    # Arrange
    cantidad, precio_unitario = 50, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(425)


def test_volumen_exactamente_100_da_20_por_ciento():
    # Arrange
    cantidad, precio_unitario = 100, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(800)


def test_volumen_cantidad_negativa_lanza_error():
    # Arrange
    cantidad, precio_unitario = -1, 10
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)


def test_volumen_precio_unitario_negativo_lanza_error():
    # Arrange
    cantidad, precio_unitario = 5, -10
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)




def test_cumulativo_dos_descuentos():
    # Arrange  (100 - 50% = 50; 50 - 10% = 45)
    precio, descuentos = 100, [50, 10]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(45)


def test_cumulativo_lista_vacia_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100


def test_cumulativo_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -100, [10]
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)


def test_cumulativo_descuento_fuera_de_rango_lanza_error():
    # Arrange
    precio, descuentos = 100, [10, 120]
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)



def test_apilado_suma_porcentajes():
    # Arrange  (10% + 20% = 30% sobre 100)
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(70)


def test_apilado_total_mayor_a_100_queda_en_100():
    # Arrange  (revela el BUG 2: 60% + 50% = 110%, debe limitarse a 100%)
    precio, descuentos = 100, [60, 50]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0


def test_apilado_descuento_negativo_lanza_error():
    # Arrange  (un descuento negativo encarecería el producto)
    precio, descuentos = 100, [30, -10]
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)


def test_apilado_lista_vacia_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100


def test_apilado_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -100, [10]
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)