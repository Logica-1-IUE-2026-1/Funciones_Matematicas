"""
    Esta es la función integradora que va a reunir todas las funciones 
    matematicas y las va a ejecutar pro medio de la función main
"""

import circulo
import cuadrado
import rectangulo
import triangulo
import trapecio_area
import trapecio_perimetro


def main():
    """
        Función principal que ejecuta la operaciones matematicas entre dos números
    """
    # Primero vamos a llamar las operaciones del circulo
    print("Calculadora de areá y perimetro de diferentes formas\n")
    print("Vamos a iniciar con el Circulo")
    radio=int(input("Ingresa el radio\n"))#pedimos el radio del circulo

    area_circulo = circulo.area_circulo(radio)
    perimetro_circulo = circulo.perimetro_circulo(radio)

    print(f"el area del circulo es: {area_circulo}\n")
    print(f"el perimetro del circulo es: {perimetro_circulo}\n")

    # Segundo vamos a llamar las operaciones del cuadrado
    print("Continua con el cuadrado\n")
    lado_cuadrado=int(input("Ingresa un lado del cuadrado\n"))#pedimos un lado del cuadrado

    area_cuadrado = cuadrado.area_cuadrado(lado_cuadrado)
    perimetro_cuadrado = cuadrado.perimetro_cuadrado(lado_cuadrado)

    print(f"el area del cuadrado es: {area_cuadrado}\n")
    print(f"el perimetro del circulo es: {perimetro_cuadrado}\n")

    # Tercero vamos a llamar las operaciones del triangulo
    print("Continua con el triangulo\n")
    altura_triangulo=int(input("Ingresa la altura del triangulo\n"))#pedimos la altura del triangulo
    base_triangulo=int(input("Ingresa la base del triangulo (lado 1)\n"))#pedimos la base del triangulo
    lado2_triangulo=int(input("Ingresa otro lado del triangulo (lado 2)\n"))#pedimos el lado 2 triangulo
    lado3_triangulo=int(input("Ingresa el tercer lado del triangulo (lado 3)\n"))#pedimos el lado 3 del triangulo

    area_triangulo = triangulo.area_triangulo(base_triangulo,altura_triangulo)
    perimetro_triangulo = triangulo.perimetro_triangulo(base_triangulo, lado2_triangulo, lado3_triangulo)

    print(f"el area del triangulo es: {area_triangulo}\n")
    print(f"el perimetro del triangulo es: {perimetro_triangulo}\n")

    
    # Cuarto vamos a llamar las operaciones del trapecio
    print("Continua con el trapecio\n")
    base_grande=int(input("Ingresa la base grande del trapecio(lado 1)\n"))#pedimos la base grande del trapecio
    base_pequena=int(input("Ingresa la base pequeña del trapecio (lado 2)\n"))#pedimos la base pequeña del trapecio
    altura_trapecio=int(input("Ingresa la altura del trapecio\n"))#pedimos la altura del trapecio
    lado3_trapecio=int(input("Ingresa el tercer lado del trapecio (lado 3)\n"))#pedimos el lado 3 del trapecio
    lado4_trapecio=int(input("Ingresa el cuarto lado del trapecio (lado 4)\n"))#pedimos el lado 4 del trapecio

    area_trapecio = trapecio_area.area(base_grande,base_pequena,altura_trapecio)
    perimetro_trapecio = trapecio_perimetro.perimetro(base_grande,base_pequena,lado3_trapecio,lado4_trapecio)

    print(f"el area del trapecio es: {area_trapecio}\n")
    print(f"el perimetro del trapecio es: {perimetro_trapecio}\n")

    # Quinto vamos a llamar las operaciones del rectangulo
    print("Continua con el rectangulo\n")
    lado1_rectangulo=int(input("Ingresa un lado del rectangulo\n"))#pedimos un lado del rectangulo
    lado2_rectangulo=int(input("Ingresa un lado del rectangulo\n"))#pedimos un lado del rectangulo

    area_rectangulo = rectangulo.area_rectangulo(lado1_rectangulo,lado2_rectangulo)
    perimetro_rectangulo = rectangulo.perimetro_rectangulo(lado1_rectangulo,lado2_rectangulo)

    print(f"el área del rectangulo es: {area_rectangulo}\n")
    print(f"el perimetro del rectangulo es: {perimetro_rectangulo}\n")


    return 0



if __name__== "__main__":
    RESULT = main()
    if RESULT == 0:
        print("Resultado de la ejecución es exitoso")
    else:
        print("Resultado de la ejecución es fallido")
