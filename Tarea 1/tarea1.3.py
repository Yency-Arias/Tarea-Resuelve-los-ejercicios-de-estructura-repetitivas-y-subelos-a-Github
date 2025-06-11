#                      ---Contador de digitos---
#pidiendo al usuario un numero entero positivo
numero = int(input('Ingresa un numero positivo:\n'))

#verificando que el numero sea positivo
while numero <= 0:
    print('El numero debe ser mayor que 0.\n')
    numero = int(input('Por favor, ingresa un numero positivo: \n'))

#contando los digitos usando un bucle while
contador = 0
temporal = numero

while temporal > 0:
    temporal //= 10  #quitamos el ultimo digito
    contador += 1    #aumentamos el contador

#mostrando el resultado
print(f'\nEl numero {numero} tiene {contador} digitos.')