# JonathanBN
##Múltiples condiciones IF en Python
# Solicitamos al usuario que ingrese un número del 1 al 4
entrada = int(input('Introduce un número del 1 al 4:\n'))
# Verificamos la opción seleccionada
if entrada == 1:
    print('Has seleccionado la opción número 1.')
    if entrada == 2:
        print('Has seleccionado la opción número 2.')
        if entrada == 3:
            print('Has seleccionado la opción número 3.')
            if entrada == 4:
                print('Has seleccionado la opción número 4.')