import pandas as pd
ventas = pd.read_csv("data/ventas.csv")
##1. Venta promedio por sucursal
print("El promedio de las ventas por sucursal es: ")
print(ventas.groupby("sucursal")["ventas"].mean())
##2. Ticket promedios 
print("El promeido de tickets es: ", 
ventas["ventas"].sum() / ventas["clientes"].sum())
## 3. Sucursal  con mayor venta y menor venta
print("Sucursal con mayor venta es: ", 
    ventas.loc[ventas["ventas"].idxmax(), "sucursal"])
print("Sucursal con menor venta es: ", 
    ventas.loc[ventas["ventas"].idxmin(), "sucursal"])
ventas_por_region = ventas.groupby("region").sum("ventas")
print()
## 4. Mayor región que tiene ventas
ventas_por_region = ventas.groupby("region")[["ventas"]].sum().reset_index()
print(ventas_por_region)
## 4.1. Imprimir la region que tiene mas ventas 
print("La region con mas ventas es:", 
ventas_por_region.loc[ventas_por_region["ventas"].idxmax(), "region"])