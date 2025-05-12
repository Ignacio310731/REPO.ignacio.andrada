#Ingresar un número.
# Mostrar cada número primo que hay entre el 1 y el número ingresado.
# Informar cuántos números primos se encontraron.

numero = int(input("Ingrese un número: "))
cantidad_primos = 0

print("Números primos encontrados:")

for i in range(2, numero + 1):
    divisores = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisores += 1
    if divisores == 2:
        print(i)
        cantidad_primos += 1

print(f"Se encontraron {cantidad_primos} números primos entre 1 y {numero}.")
