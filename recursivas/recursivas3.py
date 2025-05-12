#Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_numeros(numeros : int):
    if numeros <= 10:
        return numeros
    else:
        return numeros % 10 + sumar_numeros(numeros // 10)

print(sumar_numeros(153))
