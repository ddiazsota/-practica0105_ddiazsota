def calcular_capital():
   
    cantidad = float(input("Ingrese la cantidad a invertir: "))
    tasa_interes = float(input("Ingrese el interés anual (en porcentaje): "))
    años = int(input("Ingrese el número de años: "))

    tasa_interes_decimal = tasa_interes / 100

    capital = cantidad * (1 + tasa_interes_decimal)**años

    print(f"\nEl capital obtenido después de {años} años es: {capital:.2f}")

calcular_capital()
