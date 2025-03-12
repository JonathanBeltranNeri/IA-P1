x = 0
while x < 30:
    # Si x es igual a 4, 6 o 10, se salta la iteración
    if x == 4 or x == 6 or x == 10:
        print('Se saltó el valor', x, 'de x')
        x += 1  # Incrementar x para evitar bucles infinitos
        continue  # Salta al siguiente ciclo del bucle

    # Si x llega a 15, se rompe el bucle
    if x == 15:
        print('Se rompió la ejecución del bucle cuando x valía', x)
        break  # Termina el bucle

    # Se imprime el valor de x
    print('El valor del bucle es:', x)
    x += 1  # Incrementa x de 1 en 1
