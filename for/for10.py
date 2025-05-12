#Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un numero: "))
contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    print(f"{numero} es numero primo")
else:
    print(f"{numero} No es numero primo")