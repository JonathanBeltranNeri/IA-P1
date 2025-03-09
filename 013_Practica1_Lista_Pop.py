## JonathanBN
# Eliminación de elementos en listas Python

# Se define una lista con colores.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Se eliminan colores de la lista usando el método pop() y se almacenan en la lista 'eliminaciones'.
eliminaciones=[colores.pop(1),colores.pop(-2)]

# Imprime la lista de colores después de las eliminaciones.
print("Lista de colores:",colores)

# Imprime los colores que fueron eliminados.
print("colores eliminados:",eliminaciones)
