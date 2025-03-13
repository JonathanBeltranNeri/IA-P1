## JonathanBN
# ¿Cómo usar diccionarios con el bucle for de Python?

# Definición del primer diccionario 'teclado1' con información sobre un teclado
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

# Definición del segundo diccionario 'teclado2' con información sobre otro teclado
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

# Bucle for para recorrer las claves del diccionario 'teclado2'
for x in teclado2:
	 # Se imprime el nombre de la clave y su valor correspondiente en 'teclado1'
	print(x,"=",teclado1[x])