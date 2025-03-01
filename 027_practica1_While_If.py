# JonathanBN
## Bucle while con condicional if
x = 0

while x <= 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print('Se saltó el valor', x, 'de x')
        continue  # Salta las ejecuciones para los valores 4, 6 y 10
    print('El valor del bucle es:', x)
    if x == 15:
        print('Se rompió la ejecución del bucle cuando x valía', x)
        break  # Sale del bucle cuando x es igual a 15
