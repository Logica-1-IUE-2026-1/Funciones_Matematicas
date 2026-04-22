"""
    Esta función nos calcula el área de un trapecio
"""
def area(Bg, Bp, H):
    """
    Esta función halla el área de un trapecio
    
    Parámetros: 
    Bg = Base grande del trapecio
    Bp = Base pequeña del trapecio 
    H = Altura del trapecio
    
    Retorna: 
    int: El area del trapecio de lados Bg, Bp, y H
    """

    res = ((Bg + Bp)/2)*H
    return res
