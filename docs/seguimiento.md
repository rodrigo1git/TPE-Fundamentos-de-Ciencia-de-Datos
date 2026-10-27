# Seguimiento del trabajo

## Estado de avance

| Inciso | Contenido | Estado |
| --- | --- | --- |
| 1 | Análisis exploratorio inicial | Desarrollado |
| 2 | Limpieza y justificación de las acciones | Código implementado; justificación y redacción final pendientes |
| 3 | Hipótesis propias: univariada, bivariada y multivariada | Pendiente |
| 4 | Validación de las seis hipótesis | Pendiente |

La notebook y el informe usan las mismas secciones. Las secciones pendientes se mantienen identificadas durante el desarrollo y deben completarse antes de la entrega.

## Inciso 2: implementación aprobada

La limpieza se realiza sobre una copia de trabajo. El Excel de origen y el DataFrame original se conservan sin modificaciones. La notebook incorpora el código operacional; los integrantes del grupo redactarán las explicaciones académicas y la justificación de las decisiones en la notebook y el informe.

### Selección de columnas

Se retiran diez columnas de la copia: las dos constantes completas y ocho códigos seleccionados, conservando las descripciones correspondientes.

| Motivo | Columnas retiradas |
| --- | --- |
| Constantes completas | `Model Year`, `FE_UNIT` |
| Códigos seleccionados | `Tested Transmission Type Code`, `Drive System Code`, `Transmission Overdrive Code`, `Shift Indicator Light Use Cd`, `Test Procedure Cd`, `Test Fuel Type Cd`, `Aftertreatment Device Cd`, `Averaging Method Cd` |

Se conserva `Veh Mfr Code` porque integra la clave de configuración. También se mantienen los nombres de fabricante, la categoría y el procedimiento de ensayo. `Averaging Weighting Factor` permanece: su único valor observado no equivale a una constante completa, ya que presenta faltantes.

### Filas y valores faltantes existentes

No se deduplican filas: la exploración identificó cero filas completamente idénticas. Tampoco se eliminan ni promedian registros por compartir `Test Number`, vehículo o configuración.

Por decisión del usuario, **no se implementa el punto 4 de la propuesta original**: no se agrega lógica de clasificación de faltantes o aplicabilidad ni se imputan los nulos existentes. Los nuevos `NaN` provienen únicamente del tratamiento de valores sospechosos aprobado.

### Tratamiento de valores sospechosos

En la copia se convierten a `NaN` los valores seleccionados de cilindrada, economía y potencia. Se incluyen la cilindrada 99.999 L, las economías 9999.9999999, 4599.1, 4595.3 y cero, las potencias de 1 HP y los candidatos a atípicos de economía del grupo gasolina Tier 2 con procedimiento `Federal fuel 2-day exhaust (w/can load)`.

La exploración identificó **68 candidatos** mediante el criterio Q1 − 1,5 × RIC / Q3 + 1,5 × RIC en ese grupo. Son candidatos descriptivos, **no errores confirmados**. Su conversión a `NaN` responde a la decisión aprobada por el usuario. Tampoco se afirma que los demás valores seleccionados sean códigos especiales de ausencia confirmados.

### Resultados verificados

La ejecución completa finalizó correctamente. Se conservaron **4.287 filas, 1.448 configuraciones y 4.014 números de ensayo distintos**. La selección redujo las columnas de **67 a 57**. No se eliminaron filas y el recuento de filas completamente duplicadas sigue siendo **cero**.

| Variable | Nulos antes | Nuevos `NaN` | Nulos después |
| --- | ---: | ---: | ---: |
| `Test Veh Displacement (L)` | 0 | 95 | 95 |
| `Rated Horsepower` | 0 | 8 | 8 |
| `RND_ADJ_FE` | 221 | 80 | 301 |

Las 80 conversiones de economía incluyen los 12 casos específicos y los **68 índices del criterio del boxplot**. En total se modificaron **183 celdas en 183 filas distintas**. Se comprobó que el Excel original permanece intacto y que todas las demás columnas conservadas mantienen sus valores.

## Próximos pasos

- Redactar y justificar las acciones del inciso 2 en la notebook y el informe.
- Definir la unidad de análisis y la selección de ensayos para cada hipótesis.
- Formular las tres hipótesis propias y desarrollar las seis validaciones.

## Control final de entrega

- [ ] Inscripción del grupo completada, con no más de tres integrantes.
- [ ] Una única notebook con todos los incisos completos y organizada en secciones.
- [ ] Notebook ejecutada desde un kernel nuevo, sin errores y con resultados guardados.
- [ ] Sin pruebas descartadas, borradores, instrucciones pendientes ni celdas de depuración.
- [ ] Limpieza documentada y justificada.
- [ ] Tres hipótesis propias justificadas y seis hipótesis evaluadas.
- [ ] Técnicas y condiciones de aplicación explicadas, con discusión de resultados.
- [ ] Informe completo, consistente con los resultados y con referencias explícitas a las secciones de la notebook.
- [ ] Archivo de datos incluido y sin modificaciones respecto del original.
- [ ] `requirements.txt` actualizado y sin conflictos de dependencias.
- [ ] README probado para reconstruir y ejecutar el proyecto localmente.
- [ ] `.venv`, credenciales, cachés y archivos temporales excluidos de Git.
- [ ] Archivos finales publicados y accesibles para la cátedra mediante el enlace del repositorio.
- [ ] Entrega realizada antes del 10/11/2026 a las 23:59.

## Condiciones de evaluación

La falta de entregables o de código ejecutable puede ser penalizada o requerir reentrega. La defensa es grupal y presencial, con calificación individual según las respuestas de cada integrante. El informe no tiene límite de páginas. El enunciado permite utilizar un template como guía, sin imponerlo como formato obligatorio.
