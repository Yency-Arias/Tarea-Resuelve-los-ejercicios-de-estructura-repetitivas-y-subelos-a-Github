#                ---Creando serie de Fibonacci---
#pidiendo al usuario el numero de terminos
n = int(input('Ingresa el numero de terminos de la serie de Fibonacci:\n'))

#verificando que n sea positivo
while n <= 0:
    print('El numero debe ser mayor que 0.\n')
    n = int(input('Ingresa el numero de terminos de la serie de Fibonacci:\n'))

#inicializando los dos primeros terminos
a, b = 0, 1

print('Serie de Fibonacci: \n')
for i in range(n):
    print(a)
    a, b = b, a + b
