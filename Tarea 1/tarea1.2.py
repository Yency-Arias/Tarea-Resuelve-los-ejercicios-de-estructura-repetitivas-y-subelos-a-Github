#                     ---Numeros pares del 1 al 20---
#generando los numeros con range
print('Numeros pares del 1 al 20:\n')
for numero in range(1, 21):
    
    #verificando si el numero es par
    if numero % 2 == 0:
        
        #imprimiendo numeros
        print(numero)