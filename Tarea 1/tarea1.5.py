#                           ---Conteo regresivo---
#pidiendo al usuario un numero entero
numero = int(input('Ingresa un número entero:\n'))

#verificando que el numero sea positivo
while numero <= 0:
    print('El número debe ser positivo...\n')
    numero = int(input('Por favor, ingresa un número positivo:\n'))

#imprimimos los numeros en orden descendente hasta 0
while numero >= 0:
    print(numero)
    numero -= 1
print('\nConteo regresivo terminado.')