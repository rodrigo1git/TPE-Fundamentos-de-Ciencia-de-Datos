# Seguimiento del trabajo

## Estado de avance

| Inciso | Contenido | Estado |
| --- | --- | --- |
| 1 | Análisis exploratorio inicial | Desarrollado; sección 1.4 ampliada con búsqueda de representaciones alternativas de faltantes |
| 2 | Limpieza y justificación de las acciones | Código implementado y verificado; borrador de explicaciones agregado, pendiente de validación del grupo |
| 3 | Hipótesis propias: univariada, bivariada y multivariada | Pendiente |
| 4 | Validación de las seis hipótesis | Pendiente |

La notebook y el informe usan las mismas secciones. Las secciones pendientes se mantienen identificadas durante el desarrollo y deben completarse antes de la entrega.

## Ampliación del inciso 1.4: otras representaciones de faltantes

Se amplía la exploración siguiendo el trabajo con `value_counts()` de la práctica 4: además de contar `NaN`, se examinan valores repetidos y posibles marcas alternativas de ausencia. Esta revisión describe los datos y no modifica la limpieza aprobada.

Se comprobaron **51.153 celdas vacías en el Excel**, coincidentes con el total de `NaN` de la lectura habitual. No se encontraron coincidencias con otras marcas textuales buscadas, como `na`, `n/a`, `nan`, `null` o `unknown`. Este resultado se limita a las marcas revisadas: no demuestra que todos los valores numéricos tengan un significado válido ni descarta otras convenciones no documentadas.

Se identificaron los siguientes casos para revisar:

| Variable o grupo | Observación | Estado |
| --- | --- | --- |
| `PM (g/mi)` | 15 valores iguales a 9999.9999999 | Nuevo candidato a valor especial o inconsistencia; no se confirmó que represente ausencia. |
| Tres calificaciones DT | El valor −1 aparece 5, 6 y 2 veces en las tres columnas; también existen otros valores negativos. | Pendiente de interpretación; el signo negativo no basta para clasificarlo como faltante. |
| `Set Coef A (lbf)` | 4 valores iguales a 99.999 | Pendiente de interpretación; no se aplica a esta columna el criterio utilizado para cilindrada. |
| `Test Veh Displacement (L)` | 95 valores iguales a 99.999 | Caso ya identificado en el análisis anterior. |
| `RND_ADJ_FE` | 8 valores iguales al máximo 9999.9999999 | Caso ya identificado en el análisis anterior. |

Los nuevos candidatos **no se reemplazan por `NaN` ni se incorporan a las reglas del inciso 2**. Tampoco se interpreta automáticamente un valor como ausente por coincidir numéricamente con uno seleccionado en otra variable. El tratamiento de cilindrada y economía previamente aprobado se conserva; la nueva búsqueda deja pendientes de revisión los valores de PM, DT y coeficiente A.

## Inciso 2: implementación aprobada

La limpieza se realiza sobre una copia de trabajo. El Excel de origen y el DataFrame original se conservan sin modificaciones. La notebook incorpora el código operacional y un borrador de explicaciones breves antes de cada uno de los cuatro bloques del inciso 2. El grupo deberá revisar esas explicaciones y completar la justificación académica final y su desarrollo en el informe.

### Borrador de explicaciones por bloque

A pedido del usuario, se agregaron cuatro textos Markdown breves y concretos para explicar qué hace cada bloque de código:

1. Crear una copia y seleccionar las columnas que se conservan.
2. Comprobar las filas, las configuraciones y los números de ensayo.
3. Reemplazar por `NaN` los valores seleccionados, incluyendo los 68 candidatos del diagrama de caja, sin presentarlos como errores confirmados.
4. Comparar las dimensiones y los valores faltantes antes y después.

Estas explicaciones acompañan el código existente; no cambian sus operaciones ni el análisis del inciso 1. Son un **borrador pendiente de validación del grupo** y no dan por finalizada la justificación académica de la limpieza.

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

- Revisar el significado de los nuevos candidatos de PM, calificaciones DT y coeficiente A antes de proponer cambios adicionales.

- Revisar y validar en grupo las explicaciones agregadas al inciso 2.
- Completar la justificación académica final de la limpieza y su desarrollo en el informe.
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
