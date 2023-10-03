def calcular_ganancia(barras_vendidas):
    precio_por_barra = 3.49  
    descuento = 0.60  

    precio_normal = precio_por_barra * barras_vendidas

    precio_con_descuento = precio_normal * (1 - descuento)

    ganancia_total = precio_con_descuento

    return precio_normal, precio_con_descuento, ganancia_total

barras_vendidas_no_frescas = int(input("Ingrese el número de barras no frescas vendidas: "))

precio_normal, precio_con_descuento, ganancia_total = calcular_ganancia(barras_vendidas_no_frescas)

print(f"Precio habitual por barra: {precio_normal:.2f}€")
print(f"Descuento por barra no fresca: {(precio_normal - precio_con_descuento):.2f}€")
print(f"Ganancia total: {ganancia_total:.2f}€")
