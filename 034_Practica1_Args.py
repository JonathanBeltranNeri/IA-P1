## JonathanBN
# Explicación fácil de *args con ejemplos

# Se define la función 'colores' que acepta un número variable de argumentos
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
# Se llama a la función con dos colores como argumentos
colores("negro","blanco")

# Se define la función 'suma' que acepta un número variable de argumentos
def suma(*args):
	sumaf=(args[0]+args[1]+args[2]+args[3]+args[4]) # Suma de los primeros 5 argument
	print('El resultado de la suma es:',sumaf)

# Se llama a la función con cinco números como argumentos
suma(5,10,15,20,25)