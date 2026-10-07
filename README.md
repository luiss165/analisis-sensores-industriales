# Análisis de Sensores Industriales

## Objetivo

Analizar mediciones de temperatura y vibración obtenidas de sensores industriales instalados en cuatro plantas, con el objetivo de identificar comportamientos y detectar lecturas de temperatura consideradas como alertas.

## Datos

El proyecto utiliza un conjunto de datos simulado con 100,000 registros.

Las principales columnas son:

- `id_registro`: identificador de la medición.
- `fecha_hora`: fecha y hora de la lectura.
- `id_sensor`: identificador del sensor.
- `planta`: planta donde está instalado el sensor.
- `temperatura_c`: temperatura en grados Celsius.
- `vibracion_mm_s`: vibración en milímetros por segundo.

Los datos utilizados en este proyecto son simulados.

## Requisitos

- Python 3
- pandas
- numpy

## Instalación

### 1. Crear un entorno virtual

```bash
python -m venv .venv

### 2. Activar el entorno virtual en Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1