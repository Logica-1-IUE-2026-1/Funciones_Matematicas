l1 = int(input("Ingrese el lado 1: "))
l2 = int(input("Ingrese el lado 2: "))
l3 = int(input("Ingrese el lado 3: "))
l4 = int(input("Ingrese el lado 4: "))

def perimetro(l1, l2, l3, l4):
    """
    Esta función halla el perimetro de un trapecio
    
    Parámetros: 
    l1 = Lado 1
    l2 = Lado 2
    l3 = Lado 3
    l4 = Lado 4
    
    Retorna: 
    int: La suma de l1, l2, l3, l4
    """
    
    res = l1 + l2 + l3 + l4 
    return res

Perimetro = perimetro(l1, l2, l3, l4)
print(f'El perimetro del trapecio {l1} + {l2} + {l3} + {l4} es: {Perimetro}')