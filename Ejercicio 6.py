n = int(input("Introduce un entero positivo: "))

if n <= 0:
    print("Por favor, ingresa un entero positivo.")
else:
    suma = n * (n + 1) // 2

    print(f"La suma de los primeros {n} enteros positivos es: {suma}")

