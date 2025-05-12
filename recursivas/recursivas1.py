#Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numeros: int):
    if numeros == 1: 
        return 1
    else:            
        return numeros + sumar_naturales(numeros - 1)

print(sumar_naturales(7)) 
