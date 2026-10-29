
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, trim, upper, sum as spark_sum,
    count, desc, date_format, to_timestamp
)

# 1. Iniciar Spark
spark = SparkSession.builder \
    .appName("LimpiezaYAnalisisOnlineRetail") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 2. Leer los datos originales
ruta = "/home/vboxuser/tarea3_bigdata/datos/online_retail.csv"

df = spark.read.csv(
    ruta,
    header=True,
    inferSchema=True
)

print("REGISTROS ORIGINALES:", df.count())

# 3. Limpiar espacios de la descripción
df = df.withColumn(
    "Description",
    trim(col("Description"))
)

# 4. Convertir columnas a tipos adecuados
df = df.withColumn(
    "Quantity", col("Quantity").cast("integer")
).withColumn(
    "UnitPrice", col("UnitPrice").cast("double")
).withColumn(
    "InvoiceDate",
    to_timestamp(col("InvoiceDate"), "yyyy-MM-dd HH:mm:ss")
)

# 5. Identificar registros con datos incompletos
print("REGISTROS SIN DESCRIPCION:",
      df.filter(
          col("Description").isNull() |
          (col("Description") == "")
      ).count())

print("REGISTROS CON CANTIDAD NO POSITIVA:",
      df.filter(col("Quantity") <= 0).count())

print("REGISTROS CON PRECIO NO POSITIVO:",
      df.filter(col("UnitPrice") <= 0).count())

# 6. Filtrar datos para analizar ventas positivas
ventas = df.filter(
    col("Description").isNotNull() &
    (col("Description") != "") &
    col("Quantity").isNotNull() &
    (col("Quantity") > 0) &
    col("UnitPrice").isNotNull() &
    (col("UnitPrice") > 0) &
    col("InvoiceDate").isNotNull() &
    (~upper(col("InvoiceNo").cast("string")).startswith("C"))
)

# 7. Calcular ingresos por línea de venta
ventas = ventas.withColumn(
    "Ingresos",
    col("Quantity") * col("UnitPrice")
)

print("REGISTROS VALIDOS PARA EL ANALISIS:", ventas.count())

# 8. Mostrar los productos más vendidos por cantidad
print("PRODUCTOS MAS VENDIDOS:")
ventas.groupBy("Description") \
    .agg(spark_sum("Quantity").alias("UnidadesVendidas")) \
    .orderBy(desc("UnidadesVendidas")) \
    .show(10, truncate=False)

# 9. Calcular ingresos por país
print("INGRESOS POR PAIS:")
por_pais = ventas.groupBy("Country") \
    .agg(
        spark_sum("Ingresos").alias("IngresosTotales"),
        count("*").alias("NumeroDeRegistros")
    ) \
    .orderBy(desc("IngresosTotales"))

por_pais.show(10, truncate=False)

# 10. Calcular ingresos por mes
print("INGRESOS POR MES:")
por_mes = ventas.withColumn(
    "Mes", date_format(col("InvoiceDate"), "yyyy-MM")
).groupBy("Mes") \
    .agg(spark_sum("Ingresos").alias("IngresosTotales")) \
    .orderBy("Mes")

por_mes.show(20, truncate=False)

# 11. Guardar los resultados
carpeta = "/home/vboxuser/tarea3_bigdata/resultados"

ventas.write.mode("overwrite").option("header", True) \
    .csv(carpeta + "/ventas_limpias")

por_pais.coalesce(1).write.mode("overwrite") \
    .option("header", True).csv(carpeta + "/ingresos_por_pais")

por_mes.coalesce(1).write.mode("overwrite") \
    .option("header", True).csv(carpeta + "/ingresos_por_mes")

print("ANALISIS TERMINADO. RESULTADOS GUARDADOS.")

spark.stop()
