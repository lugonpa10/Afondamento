import requests
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Configura plotly para mostrar en navegador
pio.renderers.default = "browser"

# Obtenemos JSON del servicio USGS con información de los terremotos de
# magnitud mayor de 2.5 en escala Richter de los último días
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

# Petición get con conversión a json y extrayendo lista features
data = requests.get(url).json()["features"]

# crea una lista de diccionarios con información
# relevante de cada terremoto (lugar, magnitud, latitud, longitud).
quakes = [{"Place":q["properties"]["place"],
 "Mag":q["properties"]["mag"],
 "Lat":q["geometry"]["coordinates"][1],
 "Lon":q["geometry"]["coordinates"][0]} for q in data]

# print(quakes)

# Formatea mediante pandas una lista diccionario en tablas
# Se puede cambiar el formato aunque el estándar es muy claro
df = pd.DataFrame(quakes)
print(df)

# Crea un mapa mediante plotly con ciertas características
fig = px.scatter_geo(df, lat="Lat", lon="Lon", color="Mag",
 size="Mag", title="Terremotos Mag>2.5",
 projection="natural earth")
# Lanza una navegador (se configuró plotly al principio)
# y muestra la imagen. Crea un servidor web temporal con puerto aleatorio.
fig.show()

