\# Informe de análisis de sensores industriales



\## 1. Descripción del proyecto



El proyecto consiste en analizar datos de sensores industriales mediante Python.



La empresa utiliza sensores para monitorear máquinas en cuatro plantas industriales. Cada sensor registra temperatura y vibración.



El archivo utilizado es `sensores\_industriales.csv`, el cual contiene 100,000 mediciones simuladas.



Las columnas del archivo son:



\- `id\_registro`: identificador de la medición.

\- `fecha\_hora`: fecha y hora de la lectura.

\- `id\_sensor`: identificador del sensor.

\- `planta`: planta donde está instalado el sensor.

\- `temperatura\_c`: temperatura en grados Celsius.

\- `vibracion\_mm\_s`: vibración en milímetros por segundo.



Los datos utilizados son simulados.



\---



\# 2. Resultados del análisis



El programa `analisis.py` lee el archivo CSV utilizando rutas relativas y realiza diferentes cálculos.



\## Cantidad de registros y sensores



El archivo contiene 100,000 mediciones de sensores industriales.



El análisis también identifica la cantidad de sensores distintos presentes en el archivo.



\## Temperatura promedio por planta



Los resultados obtenidos fueron:



| Planta | Temperatura promedio |

|---|---:|

| Planta\_1 | 66.616297 °C |

| Planta\_2 | 66.534989 °C |

| Planta\_3 | 66.765774 °C |

| Planta\_4 | 66.668966 °C |



La Planta\_3 presenta el promedio de temperatura más alto, con aproximadamente \*\*66.77 °C\*\*.



\## Temperatura máxima



La temperatura máxima encontrada fue de:



\*\*104.99 °C\*\*



Debido a que existen empates, se muestran todos los sensores y fechas correspondientes:



| Sensor | Fecha |

|---|---|

| S023 | 01/09/26 22:23 |

| S019 | 02/09/26 13:11 |

| S014 | 02/09/26 15:23 |

| S030 | 02/09/26 16:02 |



\## Lecturas con temperatura mayor a 85 °C



Se encontraron:



\*\*6,954 lecturas\*\*



con una temperatura mayor a 85 °C.



\## Alertas por planta



| Planta | Alertas |

|---|---:|

| Planta\_1 | 1,737 |

| Planta\_2 | 1,708 |

| Planta\_3 | 1,777 |

| Planta\_4 | 1,732 |



La planta con más alertas es:



\*\*Planta\_3, con 1,777 alertas.\*\*



Las lecturas que superan los 85 °C fueron exportadas al archivo:



`resultados/alertas.csv`



\---



\# 3. Las 5 V de Big Data aplicadas al proyecto



| V | Relación con el proyecto | Ejemplo | Situación |

|---|---|---|---|

| Volumen | El archivo contiene una gran cantidad de mediciones de sensores. | Aumentar de 100,000 registros a millones. | Presente actualmente |

| Velocidad | Las mediciones pueden llegar continuamente desde los sensores. | Recibir datos cada segundo. | Futura ampliación |

| Variedad | Actualmente se utilizan datos organizados en columnas. | Incorporar fotografías y reportes de mantenimiento. | Futura ampliación |

| Veracidad | Es importante revisar que las mediciones sean confiables. | Detectar temperaturas anormales. | Se puede analizar actualmente |

| Valor | Los datos permiten obtener información útil para tomar decisiones. | Identificar la planta con más alertas. | Presente actualmente |



Los 100,000 registros no convierten automáticamente al archivo en Big Data. Big Data también considera características como volumen, velocidad, variedad, veracidad y valor.



Al aumentar la cantidad de sensores y recibir mediciones cada segundo, podrían aparecer problemas relacionados con almacenamiento, procesamiento, transferencia de información y tiempo de análisis.



\---



\# 4. Tipos de datos y procesamiento tradicional



\### CSV de sensores



Es un dato \*\*estructurado\*\*, porque está organizado en filas y columnas con campos definidos.



\### Mensaje JSON enviado por un sensor



Es un dato \*\*semiestructurado\*\*, porque utiliza claves y valores y permite cierta flexibilidad en su estructura.



\### Fotografía de una máquina



Es un dato \*\*no estructurado\*\*, porque una imagen no está organizada naturalmente en filas y columnas.



\### Texto libre de un reporte de mantenimiento



Es un dato \*\*no estructurado\*\*, porque no sigue una estructura tabular fija.



\## Limitaciones al aumentar la escala



Tener 100,000 registros no significa automáticamente que se tenga Big Data. También se deben considerar la velocidad de generación de los datos, la variedad de formatos y las necesidades de procesamiento.



Si el sistema aumenta a miles de sensores y recibe mediciones cada segundo, podrían ser necesarias soluciones con mayor capacidad de almacenamiento, procesamiento y transmisión.



\---



\# 5. Batch y Streaming



\## Tipo de procesamiento utilizado



El programa actual utiliza \*\*procesamiento Batch\*\*, porque analiza un archivo CSV que ya se encuentra almacenado.



El programa primero recibe los datos almacenados y posteriormente procesa el conjunto completo.



\## Alerta de temperatura mayor a 85 °C



Para emitir una alerta pocos segundos después de recibir una lectura mayor a 85 °C utilizaría \*\*Streaming\*\*.



Streaming permite procesar las lecturas conforme llegan y generar una respuesta rápidamente.



Esto sería adecuado porque una alerta de temperatura requiere una respuesta cercana al momento en que ocurre.



\## Resumen al terminar el día



Para generar un resumen al terminar el día utilizaría \*\*Batch\*\*.



Se podrían procesar todas las lecturas acumuladas durante el día para obtener:



\- Temperatura promedio.

\- Temperatura máxima.

\- Cantidad de alertas.

\- Alertas por planta.

\- Estadísticas de los sensores.



En este caso no es necesario obtener el resultado inmediatamente, por lo que Batch es adecuado.



\---



\# 6. Lambda y Kappa



\## Escenario A: Arquitectura Lambda



Para combinar una ruta que recalcule el historial por lotes con otra que procese rápidamente las mediciones recientes utilizaría una \*\*arquitectura Lambda\*\*.



```text

&#x20;             DATOS DE SENSORES

&#x20;                    |

&#x20;         +----------+----------+

&#x20;         |                     |

&#x20;         v                     v

&#x20;  BATCH / HISTORIAL       STREAMING / RECIENTE

&#x20;         |                     |

&#x20;         v                     v

&#x20;  PROCESAMIENTO          PROCESAMIENTO

&#x20;     POR LOTES             RÁPIDO

&#x20;         |                     |

&#x20;         +----------+----------+

&#x20;                    |

&#x20;                    v

&#x20;                RESULTADOS



Escenario B: Arquitectura Kappa

Para utilizar una sola lógica de procesamiento de eventos y conservar las mediciones para volver a procesarlas utilizaría una arquitectura Kappa.

&#x20;      SENSORES

&#x20;         |

&#x20;         v

&#x20;  FLUJO DE EVENTOS

&#x20;         |

&#x20;         v

&#x20;    PROCESAMIENTO

&#x20;         |

&#x20;         v

&#x20;     RESULTADOS

&#x20;         |

&#x20;         |

&#x20;  REPROCESAMIENTO

&#x20;         |

&#x20;         +--------> FLUJO DE EVENTOS

7\. Analítica descriptiva, predictiva y prescriptiva

Analítica descriptiva

El análisis permite conocer lo que ocurrió en los datos.

Dos hallazgos importantes son:

1\. La Planta\_3 tiene la temperatura promedio más alta, con aproximadamente 66.77 °C.

2\. La Planta\_3 tiene la mayor cantidad de alertas, con 1,777 lecturas mayores a 85 °C.

Además, se encontraron 6,954 lecturas con temperatura superior a 85 °C.

Analítica predictiva

Una pregunta predictiva podría ser:

¿Qué sensores o plantas podrían presentar más lecturas superiores a 85 °C en el futuro?

Para investigar esta pregunta sería necesario contar con datos adicionales como:

\- Historial de mantenimiento.

\- Historial de fallas.

\- Tipo de máquina.

\- Carga de trabajo.

\- Tiempo de funcionamiento.

\- Mediciones de sensores durante periodos más largos.

Una lectura mayor a 85 °C representa una alerta del ejercicio, pero por sí sola no demuestra que una máquina vaya a fallar.

Analítica prescriptiva

Una posible acción sería aumentar la frecuencia de inspección de las máquinas que presenten repetidamente temperaturas elevadas.

Antes de tomar esta decisión se deberían revisar:

\- Historial de mantenimiento.

\- Cantidad de alertas.

\- Duración de las temperaturas elevadas.

\- Estado de la máquina.

\- Historial de fallas.

\- Condiciones de operación.

La decisión no debería basarse solamente en una lectura aislada.

8\. Conclusión

El análisis permitió procesar 100,000 mediciones simuladas de sensores industriales.

Los resultados muestran que la Planta\_3 presenta el promedio de temperatura más alto y también la mayor cantidad de alertas.

Actualmente el proyecto utiliza procesamiento Batch debido a que trabaja con un archivo CSV almacenado. Sin embargo, si el sistema comienza a recibir mediciones cada segundo, sería conveniente utilizar Streaming para generar alertas rápidamente.

La incorporación de más sensores, diferentes tipos de datos y una mayor velocidad de generación de información podría aumentar la necesidad de utilizar tecnologías y arquitecturas de Big Data.

El análisis descriptivo permite conocer lo ocurrido, mientras que el análisis predictivo y prescriptivo puede ayudar posteriormente a anticipar riesgos y apoyar la toma de decisiones.

