# JonathanBN
## El condicional if elif else 
# Solicita la edad al usuario
edad = int(input('¿Cuál es tu edad?\n'))

# Verifica el rango de edad con condiciones
if edad <= 0:
    print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
    print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
    print("Eres mayor de edad.")
elif edad > 45 and edad <= 100:
    print('Eres mayor de edad.')
elif edad > 100 and edad <= 120:
    print("Eres mayor de edad.")
else:
    print('Edad no válida.')
