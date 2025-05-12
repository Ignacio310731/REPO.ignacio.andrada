#Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def numero(numero1):
    if numero1 % 2 == 0:
        return True
    else:
        return False


print(numero(19))
