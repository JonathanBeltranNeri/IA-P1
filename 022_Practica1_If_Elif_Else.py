## JonathanBN
# El condicional if elif else y entrada de datos

# Se solicita la edad del usuario como entrada y se convierte a tipo entero
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
    # Si la edad es menor o igual a 0, se imprime un mensaje indicando que no es válida
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	# Si la edad está entre 1 y 18 años, se imprime que es menor de edad
	print('Eres menor de edad.')
elif edad >= 18 and edad<= 45:
    # Si la edad está entre 18 y 45 años, se indica que es mayor de edad y está en el rango de 18 a 45 años
	print("Eres mayor de edad estan en una rango de 18 a 45 años")
elif edad >= 18 and edad <= 100:
    # Si la edad está entre 18 y 100 años, se indica que es mayor de edad
	print('Eres mayor de edad.')
elif edad>= 100 and edad <=120:
    # Si la edad está entre 100 y 120 años, se indica que es mayor de edad y está en ese rango
	print("Eres mayor de edad y estas en un rago de 100 a 120 años")
else:
    # Si la edad es mayor a 120 años, se imprime un mensaje de edad no válida
	print('Edad no válida.')