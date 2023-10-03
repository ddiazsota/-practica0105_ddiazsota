def calcular_peso_total(payasos, munecas):
    peso_payaso = 112  
    peso_muneca = 75   
    peso_total = (payasos * peso_payaso) + (munecas * peso_muneca)

    return peso_total

payasos = int(input("Ingrese el número de payasos vendidos: "))
munecas = int(input("Ingrese el número de muñecas vendidas: "))

peso_total = calcular_peso_total(payasos, munecas)

print(f"El peso total del paquete que será enviado es de {peso_total} gramos.")
