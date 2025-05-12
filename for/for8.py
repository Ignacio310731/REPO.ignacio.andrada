#Realizar un programa que permita mostrar una pirámide de números.
# Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
n = int(input("ingrese un numero para hacer la piramide: "))
for i in range(1,n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()