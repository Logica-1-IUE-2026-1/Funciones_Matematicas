"""
    Esta función nos calcula el área y el perimetro de un trapecio
"""
def area(baseg, basep, altura):
    """
    Esta función halla el área de un trapecio
    
    Parámetros: 
    baseg (int) :Base grande del trapecio
    basep (int) : Base pequeña del trapecio 
    altura (int): Altura del trapecio
    
    Retorna: 
    int: El area del trapecio de lados Bg, Bp, y H
    """

    z = ((baseg + basep)/2)* altura
    return z

def perimetro(lado1, lado2, lado3, lado4):
    """
    Esta función halla el perimetro de un trapecio
    
    Parámetros: 
    (int): Lado 1
    (int): Lado 2
    (int): Lado 3
    (int): Lado 4
    
    Retorna: 
    int: La suma de l1, l2, l3, l4
    """

    z = lado1 + lado2 + lado3 + lado4
    return z
