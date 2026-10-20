# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Lo que recibí fueron tres reportes de las ventas en formatos distintos para su repectivo analísis. Al trabajarlos en Python pude constatar que la información de esa semana coincidía en cada uno. La sucursal con mayores ventas es Guayaquil Centro y la región con mayores ventas es la Sierra. La recomendación es usar los tres reportes para el intercambio de información de esa semana pero es preferible hacer uso del archivo ventas.csv por su facilidad de manejo.

## 1. ¿Los tres formatos contienen la misma información?

*Carga los tres archivos (CSV, JSON y Excel) en Python y en R, y compara dimensiones y estructura. Completa la tabla:*

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | ventas = pd.read_csv("data/ventas.csv")|
| JSON | API de fidelización | 5 | 4| with open("data/ventas.json", encoding="utf-8") as f: datos = json.load(f), ventas = pd.json_normalize(datos)|
| Excel | Consolidado de finanzas |5 |4 | ventas = pd.read_excel("data/ventas.xlsx") |

*Responde: ¿la estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?*

No existe ningún cambio en el contenido, solamente cambia el formato pero los datos siguen intactos.

## 2. Tipos de datos y calidad

*Inspecciona los tipos que infiere cada lenguaje. Completa la tabla y comenta si los tipos son los esperados para cada variable:*

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | int(64) | numeric | Número entero: se puede realizar cálculos como el promedio o la suma.|
| `clientes` | int(64) | numeric | Número entero: se puede realizar cálculos como el promedio o la suma.|
| `sucursal` | object | character | Texto: indica el nombre de cada sucursal.|
| `region` | object | character | Texto: indica el nombre de cada región.|

*¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?*

 Lo que habría indicado es el cambio del tipo de la columna y posterior a ello, hubiésen surgido errores para los cálculos que se requerían.

## 3. Particularidades técnicas encontradas

*Anota qué encontraste al leer cada formato (una nota por formato): ¿el JSON llegó como tabla? ¿hubo que indicar una hoja en el Excel? ¿cómo se expresan las categóricas en cada lenguaje?*

Como primer punto, el formato JSON al leerlo tuve que aplanarlo para poder trabajarlo con un DataFrame ya que vino como un diccionario con su clave-valor. En cambio en el reporte de Excel se leyó directamente el documento para transformarlo en un DataFrame pero allí se usó la función sheet_name para indicar la hoja de Excel que se necesitaba usar. Finalmente al leer el reporte CSV no se presentó nignuna dificultad realicé ningún paso extra como lo fue con los anteriores formatos. En Python las variables categóricas como sucursal y región son expresadas como object, mientras qué, en R, esas mismas variables se las catalogan como character.

## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal |Cuenca: 8540, Guayaquil Centro: 15200, Guayaquil Norte: 13980, Quito Norte: 12450, Quito Sur:  |
| Ticket promedio (ventas ÷ clientes) | 38.07 |
| Sucursal con mayor venta | Guayaquil centro con 15200|
| Sucursal con menor venta | Cuenca con 8540|
| Región con mayor venta total | Sierra con 30860|

## 5. Conclusiones y recomendación

1. Los tres reportes trabajaron bajo la misma estructura de 5 filas y 4 columna. A su vez, la información es igual en cada una debido a qué solo cambia el formato más no su contenido.

2. La columnas de ventas y clientes fueron tratados como enteros, por lo que permite realizar cálculos como los promedios.

3. Finalmente, el promedio de tickets es de 38.07, la sucursal con mayores ventas es Guayaquil Centro con 15200, la sucursal con menores ventas es Cuenca con 8540 y la región con mayres ventas es la Sierra con 30860. Estos datos que calculé serán escenciales para la empresa y su escalabilidad a futuro.

Recomendación: Trabajar directamente con el reporte en formato CSV para mayor facilidad. De esta manera no se necesitará integrar más pasos para la lectura del reporte.

