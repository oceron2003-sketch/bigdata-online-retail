
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# Carpetas del proyecto
base = "/home/vboxuser/tarea3_bigdata"
resultados = base + "/resultados"
graficos = resultados + "/graficos"

os.makedirs(graficos, exist_ok=True)

def leer_resultado(carpeta):
    ruta = resultados + "/" + carpeta + "/part-*.csv"
    archivos = glob.glob(ruta)

    if not archivos:
        raise FileNotFoundError(
            "No se encontraron archivos CSV en: " + ruta
        )

    return pd.concat(
        [pd.read_csv(archivo) for archivo in archivos],
        ignore_index=True
    )

# 1. Gráfico de ingresos mensuales
meses = leer_resultado("ingresos_por_mes")
meses = meses.sort_values("Mes")

plt.figure(figsize=(12, 6))
plt.plot(
    meses["Mes"],
    meses["IngresosTotales"],
    marker="o"
)
plt.title("Ingresos por mes - Online Retail")
plt.xlabel("Mes")
plt.ylabel("Ingresos (libras esterlinas)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(graficos + "/ingresos_por_mes.png", dpi=150)
plt.close()

# 2. Gráfico de ingresos por país
paises = leer_resultado("ingresos_por_pais")
paises = paises.nlargest(10, "IngresosTotales")
paises = paises.sort_values("IngresosTotales")

plt.figure(figsize=(10, 6))
plt.barh(paises["Country"], paises["IngresosTotales"])
plt.title("Diez países con mayores ingresos")
plt.xlabel("Ingresos (libras esterlinas)")
plt.ylabel("País")
plt.tight_layout()
plt.savefig(graficos + "/ingresos_por_pais.png", dpi=150)
plt.close()

# 3. Gráfico de productos más vendidos
ventas = pd.read_csv(
    base + "/resultados/ventas_limpias/part-*.csv"
) if False else None

# Leer las ventas limpias generadas por Spark
archivos_ventas = glob.glob(
    resultados + "/ventas_limpias/part-*.csv"
)

if not archivos_ventas:
    raise FileNotFoundError(
        "No se encontraron los archivos de ventas limpias"
    )

ventas = pd.concat(
    [pd.read_csv(a) for a in archivos_ventas],
    ignore_index=True
)

productos = (
    ventas.groupby("Description", as_index=False)["Quantity"]
    .sum()
    .nlargest(10, "Quantity")
    .sort_values("Quantity")
)

plt.figure(figsize=(10, 7))
plt.barh(productos["Description"], productos["Quantity"])
plt.title("Diez productos con más unidades vendidas")
plt.xlabel("Unidades vendidas")
plt.ylabel("Producto")
plt.tight_layout()
plt.savefig(graficos + "/productos_mas_vendidos.png", dpi=150)
plt.close()

print("Visualizaciones generadas correctamente.")
print("Carpeta:", graficos)
print("Archivos creados:")
for archivo in glob.glob(graficos + "/*.png"):
    print(archivo)
