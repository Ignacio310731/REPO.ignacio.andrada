#Realizar una función para calcular el número de Fibonacci de un número ingresado por consola.
#  La función deberá seguir el siguiente prototipo:

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicita el número al usuario


numero = int(input("Ingrese un número para calcular su Fibonacci: "))
resultado = fibonacci(numero)
print(f"El número de Fibonacci en la posición {numero} es {resultado}")
