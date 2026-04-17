#Carga de Datos:

#Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
#«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
#«producto»: una cadena de texto que represente el nombre del producto vendido.
#«cantidad»: un número entero que represente la cantidad de productos vendidos.
#«precio»: un número flotante que represente el precio unitario del producto.

ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 3, "precio": 1200.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 2, "precio": 1200.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 4, "precio": 45.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 3, "precio": 25.0},
    {"fecha": "2024-01-03", "producto": "Teclado", "cantidad": 2, "precio": 45.0},
]

"""
1_
Cálculo de Ingresos Totales:
Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas.
Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.
"""
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print(f"Ingresos Totales: ${ingresos_totales}")
    
"""
2_
Análisis del Producto Más Vendido:
Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
"""
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print(f"Producto más vendido: {producto_mas_vendido}")

"""
3_
Promedio de Precio por Producto:
Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas.
Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
"""
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    precio = venta["precio"]
    cantidad = venta["cantidad"]
    if producto in precios_por_producto:
        suma_precios, cantidad_total = precios_por_producto[producto]
        suma_precios += precio * cantidad
        cantidad_total += cantidad
        precios_por_producto[producto] = (suma_precios, cantidad_total)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

"""
4_
Ventas por Día:
Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
"""
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    precio = venta["precio"]
    cantidad = venta["cantidad"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += precio * cantidad
    else:
        ingresos_por_dia[fecha] = precio * cantidad
print("Ingresos por día:")
for fecha, ingresos in ingresos_por_dia.items():
    print(f"{fecha}: ${ingresos}")
    

"""
5_
Representación de Datos:
Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
«cantidad_total»: la cantidad total vendida del producto.
«ingresos_totales»: los ingresos totales generados por la venta del producto.
«precio_promedio»: el precio promedio de venta del producto.
"""
resumen_ventas = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += precio * cantidad
        resumen_ventas[producto]["precio_promedio"] = resumen_ventas[producto]["ingresos_totales"] / resumen_ventas[producto]["cantidad_total"]
    else:
        resumen_ventas[producto] = {
                "cantidad_total": cantidad,
                "ingresos_totales": precio * cantidad,
                "precio_promedio": precio
            }
print(f"{'Producto':<15} | {'Cant. Total':<12} | {'Ingresos':<12} | {'Promedio':<10}")
print("-" * 60)

for producto, datos in resumen_ventas.items():
    print(f"{producto:<15} | {datos['cantidad_total']:<12} | ${datos['ingresos_totales']:<11,.2f} | ${datos['precio_promedio']:<9,.2f}")