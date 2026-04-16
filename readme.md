IA Log
Introducción

Durante el desarrollo del trabajo práctico se utilizó inteligencia artificial como apoyo para la generación de código, análisis conceptual y redacción de informes. A continuación, se documentan los prompts utilizados, los resultados obtenidos y el análisis crítico de cada interacción.

Prompt 1 — Generación del monolito en FastAPI
Prompt utilizado
Generame un main.py en FastAPI con 4 endpoints: inventario, pagos, usuarios y notificaciones. Cada endpoint debe simular procesamiento usando asyncio.sleep(3).

Resultado de la IA

La IA generó un archivo main.py con los 4 endpoints correctamente definidos utilizando FastAPI y asyncio.sleep(3) para simular latencia.

Correcciones realizadas
Se ajustaron los nombres de los endpoints para que coincidan exactamente con lo pedido.
Se eliminaron componentes innecesarios (como integración con base de datos) que no eran requeridos en el TP.
Justificación

La consigna pedía un monolito simple para pruebas de carga. Incluir lógica adicional (como SQLAlchemy) agregaba complejidad innecesaria y generaba errores.

Prompt 2 — Interpretación de resultados
Prompt utilizado
Explicame que significa el resultado de un test de carga en locust con tiempos de respuesta de 3000 ms.
Resultado de la IA

La IA explicó correctamente que los tiempos de respuesta estaban relacionados con el asyncio.sleep(3) y que la concurrencia permite procesar múltiples requests simultáneamente.

Correcciones realizadas
Se adaptó la explicación al contexto del TP.
Se simplificó el lenguaje para enfocarlo en impacto práctico y no solo teórico.
Justificación

El trabajo requería un análisis aplicado, no solo conceptual. Se priorizó explicar cómo afecta esto al rendimiento del sistema.
Prompt 4 — Análisis CAP (Ejercicio 2)
Prompt utilizado
Explicame el teorema CAP aplicado a un sistema de inventario y notificaciones.
Resultado de la IA

La IA explicó el teorema CAP (Consistencia, Disponibilidad y Tolerancia a particiones) y propuso ejemplos generales.

Correcciones realizadas
Se adaptó el análisis a los módulos específicos del TP:
Inventario → Consistencia + Tolerancia a particiones (CP)
Notificaciones → Disponibilidad + Tolerancia a particiones (AP)
Se agregaron ejemplos concretos de impacto en el usuario.
Justificación

La respuesta original era muy teórica. Se requería justificar decisiones arquitectónicas basadas en impacto de negocio.

Análisis crítico del uso de IA

El uso de IA permitió acelerar significativamente el desarrollo inicial del trabajo, especialmente en la generación de código base y explicaciones conceptuales. Sin embargo, se observaron las siguientes limitaciones:

Generación de soluciones innecesariamente complejas (ej: uso de base de datos no requerida)
Falta de contexto específico del TP
Necesidad de validar y adaptar cada respuesta

Por este motivo, la IA fue utilizada como herramienta de apoyo, pero todas las decisiones finales fueron analizadas y ajustadas manualmente.

Conclusión

La inteligencia artificial resultó útil como asistente técnico, pero no reemplaza el análisis crítico del desarrollador. Su uso adecuado permitió mejorar la productividad, siempre acompañado de validación y adaptación al contexto del problema.