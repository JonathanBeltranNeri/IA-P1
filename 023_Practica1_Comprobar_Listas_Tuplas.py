## JonathanBN
# Buscar datos en listas y tuplas Python

# Se define una tupla con varios colores
tupla=("morado","rojo","amarillo","azul")

# Se solicita al usuario que ingrese un color
color= input("Ingresa un color:")

# Se verifica si el color ingresado está en la tupla
if color in tupla:
     # Si el color está en la tupla, se muestra un mensaje indicando que está presente
    print("El color que has ingresado esta en la tupla")
else :
    # Si el color no está en la tupla, se muestra un mensaje indicando que no está presente
    print("El color no esta en la tupla")
