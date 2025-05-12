
cantidad = 0
suma = 0
for i in range(10):
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    cantidad +=1

if cantidad != 0:
    porcentaje = suma / cantidad 
    print(f"La suma de todos los numeros ingresados es: {suma} y el promedio es de: {porcentaje}")
else:
    print("No se ingresaron numeros validos...")