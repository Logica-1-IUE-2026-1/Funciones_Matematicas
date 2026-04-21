Bg = int(input("Ingrese la base grande: "))
Bp = int(input("Ingrese el base pequeña: "))
H = int(input("Ingrese el altura: "))

def Area(Bg, Bp, H): 
    """
    Esta función halla el perimetro de un trapecio
    
    Parámetros: 
    Bg = Base grande del trapecio
    Bp = Base pequeña del trapecio 
    H = Altura del trapecio
    
    Retorna: 
    int: El area del trapecio de lados Bg, Bp, y H
    """
    
    res = ((Bg + Bp)/2)*H
    return res

Area = Area(Bg, Bp, H)
print(f'El area del trapecio {Bg} + {Bp} / {2} * {H} es: {Area}')