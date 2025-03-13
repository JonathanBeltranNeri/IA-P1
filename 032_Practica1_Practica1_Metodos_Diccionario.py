## JonathanBN
# Métodos con diccionarios de Python

# Se define el diccionario 'teclado1' con información sobre un teclado
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
# Se define el diccionario 'teclado2' con información sobre otro teclado
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'

}

# Se elimina el diccionario 'teclado1' completamente
del teclado1,

# Se eliminan las claves 'Categoría' y 'Precio' de 'teclado2'
del teclado2['Categoría'],teclado2['Precio']

# Se imprime el diccionario 'teclado2' después de eliminar elementos
print(teclado2)