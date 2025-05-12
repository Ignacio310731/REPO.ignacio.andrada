#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def numero():
    numero1 = float(input("Ingrese un numero: "))
    return numero1

print(f"El numero ingresado es {numero()}")