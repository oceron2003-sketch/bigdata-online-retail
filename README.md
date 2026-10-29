
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



## 5. Requisitos e instalación

- Python 3.
- Apache Spark 3.5.8.
- Java compatible con la instalación de Spark.
- pandas.
- Matplotlib.

Instalar las librerías de visualización:

```bash
python3 -m pip install pandas matplotlib
```

## 6. Preparación de los datos

Descargar el conjunto de datos Online Retail de UCI:

https://archive.ics.uci.edu/dataset/352/online+retail

Convertir el archivo Excel a CSV y guardarlo como:

`/home/vboxuser/tarea3_bigdata/datos/online_retail.csv`

La conversión debe conservar los encabezados originales.

## 7. Ejecución del procesamiento por lotes

Desde la terminal de Linux:

```bash
cd ~/tarea3_bigdata/codigo
spark-submit limpieza_ventas.py
```

El programa limpia y transforma los registros, calcula los productos más vendidos y agrupa los ingresos por país y por mes.

Los resultados se guardan en:

- `resultados/ventas_limpias`
- `resultados/ingresos_por_pais`
- `resultados/ingresos_por_mes`

## 8. Generación de visualizaciones

Ejecutar:

```bash
python3 visualizar_resultados.py
```

El programa genera tres gráficas PNG:

- `ingresos_por_mes.png`
- `ingresos_por_pais.png`
- `productos_mas_vendidos.png`

Las imágenes se guardan en:

`/home/vboxuser/tarea3_bigdata/resultados/graficos`

## 9. Orden de ejecución

Primero ejecutar `limpieza_ventas.py` para crear los resultados CSV. Después ejecutar `visualizar_resultados.py` para generar las gráficas.

## 10. Autoría

Proyecto académico de procesamiento de datos con Apache Spark.
UNAD - Ingeniería de Sistemas.
