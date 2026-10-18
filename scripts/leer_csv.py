import pandas as pd
ventas = pd.read_csv("data/ventas.csv")
#Imprimir dimensiones 
print("Dimensiones: \n", ventas.shape)
#Imprimir head 
print(ventas.head())
#Tipos de datos en el DataFrame
print(ventas.dtypes)



