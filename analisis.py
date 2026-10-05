import pandas as pd

# Leer el archivo CSV
archivo = "data/sensores_industriales.csv"
df = pd.read_csv(archivo)

# 1. Cantidad de registros y sensores distintos
cantidad_registros = len(df)
cantidad_sensores = df["id_sensor"].nunique()

print("===== ANÁLISIS DE SENSORES INDUSTRIALES =====")
print()
print("Cantidad de registros:", cantidad_registros)
print("Cantidad de sensores distintos:", cantidad_sensores)

# 2. Temperatura promedio de cada planta
promedio_planta = df.groupby("planta")["temperatura_c"].mean()

print()
print("Temperatura promedio de cada planta:")
print(promedio_planta)

# 3. Temperatura máxima, sensor y fecha
temperatura_maxima = df["temperatura_c"].max()
registro_maximo = df[df["temperatura_c"] == temperatura_maxima]

print()
print("Temperatura máxima:", temperatura_maxima, "°C")
print("Sensor(es) y fecha(s) correspondientes:")

for _, fila in registro_maximo.iterrows():
    print("Sensor:", fila["id_sensor"], "| Fecha:", fila["fecha_hora"])

# 4. Lecturas con temperatura mayor a 85 °C
alertas = df[df["temperatura_c"] > 85]

print()
print("Lecturas con temperatura mayor a 85 °C:", len(alertas))

# 5. Planta con más alertas
alertas_por_planta = alertas.groupby("planta").size()

print()
print("Alertas por planta:")
print(alertas_por_planta)

mayor_numero_alertas = alertas_por_planta.max()
plantas_mayor_alerta = alertas_por_planta[
    alertas_por_planta == mayor_numero_alertas
]

print()
print("Planta(s) con más alertas:")

for planta, cantidad in plantas_mayor_alerta.items():
    print(planta, "->", cantidad, "alertas")

# 6. Exportar las alertas
alertas.to_csv("resultados/alertas.csv", index=False)

print()
print("Archivo creado: resultados/alertas.csv")