#JonathanBN
## Diccionarios con bucle for 
# Definimos el diccionario
teclado1 = {
    'Categoría': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
}

# Bucle para recorrer el diccionario
for x in teclado1:  # 'x' tomará los nombres de las claves del diccionario
    print(x+ "="+ teclado1[x]+ ".")  # Mostramos la clave y su valor
