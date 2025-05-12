#Define una función que encuentre el máximo de tres números.
#  La función debe aceptar tres argumentos y devolver el número más grande.
maximo = 0
def numero(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(f"El numero mas grande es: {numero(5,8,2)}")
