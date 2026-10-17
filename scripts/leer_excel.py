import pandas as pd
ventas = pd.read_excel("data/ventas.xlsx")
#Imprimir las dimensiones 
print("Dimensiones: ", ventas.shape)
print()
#Imprimir la tabla 
print(ventas.head())