
# Procesamiento de datos con Apache Spark - Online Retail

## 1. Descripción del proyecto

Este proyecto implementa un proceso de procesamiento por lotes
(Batch Processing) utilizando Apache Spark y PySpark sobre el
conjunto de datos Online Retail.

El objetivo es limpiar y transformar los datos de ventas,
realizar un análisis exploratorio y generar resultados que
permitan identificar productos destacados, ingresos por país
y evolución mensual de las ventas.

## 2. Tecnologías utilizadas

- Python 3
- Apache Spark 3.5.8
- PySpark
- Pandas (para la conversión inicial del archivo Excel, si aplica)
- Matplotlib (para las gráficas)

## 3. Estructura del proyecto

- `limpieza_ventas.py`: limpieza, transformación y análisis de ventas.
- `visualizar_resultados.py`: generación de gráficas.
- `README.md`: descripción e instrucciones del proyecto.

## 4. Datos utilizados

Se utiliza el conjunto de datos Online Retail de UCI Machine
Learning Repository.

Descarga los datos desde:
https://archive.ics.uci.edu/dataset/352/online+retail

Coloca el archivo convertido a CSV en la carpeta `datos` con
el nombre `online_retail.csv`.

## 5. Ejecución

1. Instalar Python y Apache Spark.
2. Preparar el archivo `online_retail.csv` en la carpeta `datos`.
3. Ejecutar el procesamiento por lotes:

   `spark-submit limpieza_ventas.py`

4. Ejecutar la generación de gráficas:

   `python3 visualizar_resultados.py`

Los scripts deben tener configuradas las rutas correspondientes
a las carpetas de datos y resultados.

## 6. Resultados esperados

- Datos de ventas limpios.
- Ingresos agrupados por país.
- Ingresos agrupados por mes.
- Gráficas de los resultados del análisis.

## 7. Autor

Estudiante de Ingeniería de Sistemas - UNAD.

## 8. Nota

Este repositorio documenta el código fuente del procesamiento.
Los archivos de datos y los resultados generados pueden mantenerse
fuera del repositorio.
