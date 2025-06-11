#                    ---Simulacion de una contraseña---
#definiendo la contraseña correcta
contrasena_correcta = 'clave123'

#inicializando una variable para almacenar la entrada del usuario
contrasena_ingresada = ''

#simulando un bucle do-while usando while
while True:
    contrasena_ingresada = input('Introduce la contraseña: ')
    if contrasena_ingresada == contrasena_correcta:
        break  #sale del bucle si la contraseña es correcta
    else:
        print('Contraseña incorrecta. Intentalo de nuevo.\n')

print('\n¡Contraseña correcta! Tienes acceso.')
