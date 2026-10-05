\# Análisis de Sensores Industriales



\## Objetivo



Analizar las mediciones de temperatura y vibración de sensores instalados en cuatro plantas industriales.



El proyecto utiliza Python y pandas para procesar el archivo CSV y obtener información sobre las temperaturas, alertas y sensores.



\## Datos



El archivo `data/sensores\_industriales.csv` contiene 100,000 mediciones simuladas.



Las columnas principales son:



\- `id\_registro`: identificador de la medición.

\- `fecha\_hora`: fecha y hora de la lectura.

\- `id\_sensor`: identificador del sensor.

\- `planta`: planta donde está instalado el sensor.

\- `temperatura\_c`: temperatura en grados Celsius.

\- `vibracion\_mm\_s`: vibración en milímetros por segundo.



Los datos utilizados en este proyecto son simulados.



\## Requisitos



\- Python 3

\- pandas



\## Instalación



Crear un entorno virtual:



```bash

python -m venv .venv

