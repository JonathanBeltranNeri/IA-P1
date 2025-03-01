# JonathanBn
## Buscar elementos en listas y tuplas
# Solicitamos al usuario que ingrese un color
entrada = input('Introduce un color:\n')

# Definimos la lista de colores
colores = ['rojo', 'amarillo', 'negro', 'blanco']

# Verificamos si el color ingresado está en la lista
if entrada in colores:
    print('El color que buscas está en la lista.')  # Se ejecuta si el color está en la lista
else:
    print('El color que buscas no está en la lista.')  # Se ejecuta si el color no está en la lista
