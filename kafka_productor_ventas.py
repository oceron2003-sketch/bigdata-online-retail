
import time
import json
import random
from kafka import KafkaProducer

productos = [
    "PAPER CRAFT, LITTLE BIRDIE",
    "MEDIUM CERAMIC TOP STORAGE JAR",
    "JUMBO BAG RED RETROSPOT",
    "WHITE HANGING HEART T-LIGHT HOLDER",
    "REGENCY CAKESTAND 3 TIER"
]

productor = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda venta: json.dumps(venta).encode("utf-8")
)

try:
    while True:
        venta = {
            "producto": random.choice(productos),
            "cantidad": random.randint(1, 5),
            "precio_unitario": round(random.uniform(2, 50), 2),
            "timestamp": int(time.time())
        }

        venta["ingresos"] = round(
            venta["cantidad"] * venta["precio_unitario"], 2
        )

        productor.send("ventas_tiempo_real", value=venta)
        productor.flush()

        print("Venta enviada:", venta)
        time.sleep(1)

except KeyboardInterrupt:
    print("Generador de ventas detenido.")

finally:
    productor.close()
