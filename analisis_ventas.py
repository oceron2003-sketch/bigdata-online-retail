from pyspark.sql import SparkSession

# 1. Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("AnalisisVentasOnlineRetail") \
    .getOrCreate()

# 2. Reducir los mensajes informativos
spark.sparkContext.setLogLevel("WARN")

# 3. Leer el archivo CSV
ruta = "/home/vboxuser/tarea3_bigdata/datos/online_retail.csv"

df = spark.read.csv(
    ruta,
    header=True,
    inferSchema=True
)

# 4. Mostrar el esquema de los datos
print("=== ESTRUCTURA DEL DATAFRAME ===")
df.printSchema()

# 5. Mostrar las primeras cinco filas
print("=== PRIMEROS CINCO REGISTROS ===")
df.show(5, truncate=False)

# 6. Contar los registros
print("=== TOTAL DE REGISTROS ===")
print(df.count())

# 7. Finalizar Spark
spark.stop()
