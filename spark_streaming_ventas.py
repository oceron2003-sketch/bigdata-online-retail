
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, from_json, from_unixtime, count, sum as spark_sum
)
from pyspark.sql.types import (
    StructType, StructField, StringType,
    IntegerType, DoubleType, LongType
)

spark = (
    SparkSession.builder
    .appName("ProcesamientoTiempoRealVentas")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# Estructura de cada venta recibida
esquema = StructType([
    StructField("producto", StringType(), True),
    StructField("cantidad", IntegerType(), True),
    StructField("precio_unitario", DoubleType(), True),
    StructField("timestamp", LongType(), True),
    StructField("ingresos", DoubleType(), True)
])

# Leer mensajes desde Kafka
mensajes = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "ventas_tiempo_real")
    .option("startingOffsets", "latest")
    .load()
)

# Convertir el mensaje JSON en columnas
ventas = (
    mensajes
    .select(
        from_json(col("value").cast("string"), esquema).alias("venta")
    )
    .select("venta.*")
    .withColumn(
        "fecha",
        from_unixtime(col("timestamp")).cast("timestamp")
    )
)

# Calcular cantidad de ventas e ingresos acumulados
resumen = ventas.agg(
    count("*").alias("cantidad_ventas"),
    spark_sum("ingresos").alias("ingresos_totales")
)

# Mostrar resultados actualizados en la terminal
consulta = (
    resumen.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", "false")
    .start()
)

print("Spark Streaming está procesando las ventas...")
consulta.awaitTermination()

