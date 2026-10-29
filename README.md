
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


## 5. Instrucciones de ejecución

### Requisitos previos

- Python 3.
- Apache Spark 3.5.8.
- Java compatible con la instalación de Spark.
- El archivo `online_retail.csv`, obtenido a partir del conjunto de datos Online Retail de UCI.

### Preparación de los datos

Crear la siguiente estructura en el entorno Linux:

```text
/home/vboxuser/tarea3_bigdata/
├── datos/
│   └── online_retail.csv
├── codigo/
│   ├── limpieza_ventas.py
│   └── visualizar_resultados.py
└── resultados/
```

El archivo CSV debe contener los encabezados originales del conjunto de datos.

### Ejecutar el procesamiento por lotes

Desde la carpeta del código, ejecutar:

```bash
cd ~/tarea3_bigdata/codigo
spark-submit limpieza_ventas.py
```

El programa limpia los datos, calcula indicadores de ventas y guarda los resultados en la carpeta `resultados`.

### Generar las gráficas

Ejecutar:

```bash
python3 visualizar_resultados.py
```

Este script genera las visualizaciones de los resultados procesados. Deben existir las dependencias de Python y las rutas configuradas en el script.

### Resultados esperados

- Ventas limpias.
- Ingresos por país.
- Ingresos por mes.
- Gráficas del análisis.

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
