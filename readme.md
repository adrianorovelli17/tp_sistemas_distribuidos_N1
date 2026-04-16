TP1 - Sistemas Distribuidos
Descripción

Este proyecto implementa un monolito en FastAPI que simula el sistema de Market-Place-Inc, con el objetivo de observar problemas de concurrencia y acoplamiento en una arquitectura no escalable.
pip install -r requirements.txt
Crear base de datos:
mysql -u root -p -e "CREATE DATABASE monolito;"
Ejecutar servidor:
uvicorn main:app --reload
Test de carga
Ejecutar Locust:
locust -f locustfile.py --host http://localhost:8000
Luego abrir:
http://localhost:8089

Configurar:

50 usuarios
spawn rate: 5

Resultados observados

Durante el test de carga se observó:

El endpoint /health mantiene latencias bajas (<20ms)
El endpoint /products aumenta significativamente su latencia
El endpoint /orders genera bloqueos en la base de datos
Problema identificado

El endpoint /orders mantiene una transacción abierta durante 3 segundos debido a asyncio.sleep(3).

Esto provoca:

Locks en la base de datos
Otros requests deben esperar
Saturación del pool de conexiones

Como todos los módulos comparten la misma base de datos, el problema afecta también al catálogo (/products), generando un acoplamiento fuerte.

Conclusión

El sistema presenta:

Cuello de botella en la base de datos
Alto acoplamiento entre módulos
Baja escalabilidad

Esto demuestra los problemas de un monolito bajo alta concurrencia.