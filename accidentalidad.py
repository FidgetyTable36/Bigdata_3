import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
from pyspark.sql import SparkSession, functions as F

# 1. Iniciar sesion en Spark
spark = SparkSession.builder.appName('BatchAccidentes').getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# 2. Cargar el dataset
df = spark.read.format('csv').option('header','true').option('inferSchema', 'true').load('file:///home/vboxuser/accidentes.csv')

print("\n--- 1. ESQUEMA DEL DATASET ---")
df.printSchema()

print("\n--- 2. LIMPIEZA: ELIMINAR NULOS Y MOSTRAR DATOS ---")
df_clean = df.dropna(subset=['GRAVEDAD', 'CLASE'])
df_clean.show(5)

print("\n--- 3. ANÁLISIS EDA: ACCIDENTES POR GRAVEDAD ---")
gravedad_count = df_clean.groupBy('GRAVEDAD').count().orderBy(F.desc('count'))
gravedad_count.show()

print("\n--- 4. ANÁLISIS EDA: ACCIDENTES POR CLASE DE CHOQUE ---")
clase_count = df_clean.groupBy('CLASE').count().orderBy(F.desc('count'))
clase_count.show()
