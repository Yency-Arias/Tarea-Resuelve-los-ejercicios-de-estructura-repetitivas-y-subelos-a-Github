#     ---Programa que cuenta hasta el numero que le demos mientras sea positivo---
#pidiendo al usuario que ingrese un numero positivo
numero = int(input('Ingresa un numero positivo:\n'))

#validando que el numero sea positivo
while numero <= 0:
    print('El numero debe ser mayor que 0\n')
    numero = int(input('Por favor, ingresa un número positivo:\n'))

#mostrando los numeros del 1 hasta el número ingresado
contador = 1
print(f'\nContando del 0 hasta {numero}')
while contador <= numero:
    print(contador)
    contador += 1

print('\nConteo finalizado.')