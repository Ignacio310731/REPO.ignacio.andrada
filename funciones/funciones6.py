#Crea una función que verifique si un número dado es par o impar. 
#La función debe imprimir un mensaje indicando si el número es par o impar.

def numero(numero1):
    if numero1 % 2 == 0:
        return "Es par"
    else:
        return "No es par"
    

print(numero(19))
