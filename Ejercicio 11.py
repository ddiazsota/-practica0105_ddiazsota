def calcular_interes(compuesto, tasa_interes, años):
    return compuesto * ((1 + tasa_interes) ** años)

cantidad_depositada = float(input("Ingrese la cantidad depositada en la cuenta de ahorros: "))

tasa_interes = 0.04

saldo_1_ano = calcular_interes(cantidad_depositada, tasa_interes, 1)

saldo_2_anos = calcular_interes(cantidad_depositada, tasa_interes, 2)

saldo_3_anos = calcular_interes(cantidad_depositada, tasa_interes, 3)

print(f"Saldo después del primer año: {saldo_1_ano:.2f}")
print(f"Saldo después del segundo año: {saldo_2_anos:.2f}")
print(f"Saldo después del tercer año: {saldo_3_anos:.2f}")
