#                 ---Calculando el factorial de un numero---
#pidiendo al usuario un numero entero no negativo
numero = int(input('Ingresa un número entero positivo:\n'))

#verificando que el numero no sea negativo
while numero < 0:
    print('El numero no puede ser negativo.\n')
    numero = int(input('Ingresa un numero entero positivo:\n'))

#calculando el factorial usando un bucle while
factorial = 1
contador = 1

while contador <= numero:
    factorial *= contador
    contador += 1

#mostrando el resultado
print(f'El factorial de {numero} es: {factorial}')
