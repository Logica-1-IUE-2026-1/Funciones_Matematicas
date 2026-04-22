"""Codigo para calcular el area y perimetro de cualquier tipo de triangulo"""

def area_triangulo(base, altura): #solicita dos parametros base y altura
    """Funcion para calcular el area de un triangulo, 
    recibe la base y la altura del triangulo y retorna el area calculada"""
    return (base * altura) / 2 #retorna el resultado de calcular el area del triangulo

def perimetro_triangulo(lado1, lado2, lado3): #solicita tres parametros lado1, lado2 y lado3
    """Funcion para calcular el perimetro de un triangulo,
    recibe los tres lados del triangulo y retorna el perimetro calculado"""
    return lado1 + lado2 + lado3 #retorna el resultado de calcular
    #el perimetro del triangulo sumando los tres lados
