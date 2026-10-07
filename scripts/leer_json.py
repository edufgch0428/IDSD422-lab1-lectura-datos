import json 
import pandas as pd
##Abrir archivos de JSON 
with open("data/ventas.json", encoding="utf-8") as f: 
    datos = json.load(f)

ventas = pd.json_normalize(datos)
print(ventas.head())
#Imprimir dimensiones 
print("Dimensiones: ", ventas.shape)
#Imprimir los tipos de cada columna 
print(ventas.dtypes)