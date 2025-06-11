#     ---Contador de numeros impares hasta el numero positivo que le demos---
#pidiendo al usuario un numero entero positivo
numero = int(input('Ingresa un numero entero positivo:\n'))

#verificando que el numero sea positivo
while numero <= 0:
    print('El número debe ser mayor que 0.\n')
    numero = int(input('Ingresa un numero entero positivo:\n'))

#inicializando el contador
contador = 1

#imprimiendo los números impares usando un bucle while
print(f'Numeros impares desde 1 hasta {numero}:')
while contador <= numero:
    print(contador)
    contador += 2