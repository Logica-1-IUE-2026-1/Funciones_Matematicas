"""
    Funciones para calcular el area y perimetro de un circulo
"""
import math
def area_circulo(radio):
    """ esta funcion calcula el area de un circulo dando su radio
    parametros = el radio del círculo
    retorna = el area del circulo con el radio dado"""
    pi = math.pi
    z = pi * radio ** 2
    return z

def perimetro_circulo(radio):
    """esta funcion calcula el perímetro de un circulo dado su radio
    parametros = el radio del círculo
    retorna = el perímetro del círculo con el radio dado"""
    pi = math.pi
    z = 2 * pi * radio
    return z
