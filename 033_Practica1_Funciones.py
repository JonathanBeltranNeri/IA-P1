## JonathanBN
# ¿Cómo crear y llamar funciones en Python?

# Se define la función 'operacion' que recibe dos números como parámetros
def operacion(numero1,numero2):
    # Se realizan tres sumas con valores adicionales
    suma1=numero1+numero2
    suma2=numero1+numero2+20
    suma3=numero1+numero2+20+56950

    # Se imprimen los resultados de cada suma
    print("El resultado de la suma es:",suma1)
    print("El resultado de la suma es:",suma2)
    print("El resultado de la suma es:",suma3)

# Se llama a la función con los valores 15 y 15
operacion(15,15)