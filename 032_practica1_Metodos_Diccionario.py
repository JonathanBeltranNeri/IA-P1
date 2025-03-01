#JonathanBN
## Metodos con diccionarios
# Definimos los diccionarios
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1# Eliminamos completamente el diccionario teclado1
del [teclado2['Categoría'],teclado2['Precio']]# Eliminamos las claves 'Categoría' y 'Precio' de teclado2
print(teclado2)# Mostramos la clave que queda en teclado2
print(len(teclado2))