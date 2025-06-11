#                        ---Tabla de multiplicacion---
#pidiendo un numero al usuario
numero = int(input('Ingresa un número para ver su tabla de multiplicar:\n'))

#imprimiendo la tabla de multiplicar del 1 al 10
print(f'Tabla de multiplicar del {numero}:\n')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')