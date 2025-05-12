#Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def numero(numero1):
    contador = 0
    for i in range(1, numero1 + 1):
        if numero1 % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

print(numero(4))