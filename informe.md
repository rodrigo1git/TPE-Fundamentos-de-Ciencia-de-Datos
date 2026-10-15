# Trabajo Práctico Especial — EPA Fuel Economy 2025

## Estado del trabajo

Se completó el análisis exploratorio inicial. La limpieza, las hipótesis propias y su validación permanecen pendientes. Las secciones de este informe se corresponden con las de `TPE.ipynb`.

## 1. Análisis exploratorio inicial

### 1.1. Contexto y lectura de los datos

**Referencia en la notebook:** sección 1.1.

EPA Fuel Economy contiene ensayos de vehículos de año modelo 2025 realizados por la Environmental Protection Agency de Estados Unidos y por fabricantes que reportan sus resultados al organismo. Estos datos forman parte del proceso de determinación de estimaciones oficiales de economía de combustible.

Se analizó el archivo `25-testcar-2026-01-21.xlsx`, hoja `Sheet1`, con **4.287 registros y 67 atributos**. La base combina características del vehículo con condiciones y resultados de ensayo. El año modelo no equivale a la fecha del ensayo. La economía se expresa en MPG, millas por galón: un valor mayor representa mayor distancia recorrida con la misma cantidad de combustible.

### 1.2. Unidad de observación y repeticiones

**Referencia en la notebook:** sección 1.2.

La combinación de `Veh Mfr Code`, `Test Vehicle ID` y `Test Veh Configuration #` identifica **1.448 configuraciones distintas**. Una configuración puede tener varios ensayos, por lo que contar filas no equivale a contar vehículos.

No hay filas completamente idénticas, pero existen **4.014 números de ensayo distintos en 4.287 registros**. `Test Number` no identifica de manera única cada fila: el ejemplo examinado muestra diferencias en el dispositivo de postratamiento. Estas filas se conservan durante la exploración. Antes de analizar configuraciones o vehículos deberá decidirse cómo tratar las repeticiones, ya que pueden dar más peso a algunos ensayos en las estadísticas.

### 1.3. Caracterización de los atributos

**Referencia en la notebook:** sección 1.3; los tipos computacionales se inspeccionan también mediante `info()` en la sección 1.1.

Se distinguieron los siguientes grupos de atributos:

- **Identificación:** fabricante, modelo, vehículo, configuración y número de ensayo. Permiten reconocer registros y entidades.
- **Cualitativos nominales:** tipo de vehículo, combustible, transmisión, tracción y procedimiento. Sus códigos también son categorías aunque estén almacenados como números. Las banderas sí/no son nominales dicotómicas.
- **Cuantitativos discretos:** cantidad de cilindros o rotores y de marchas. El año modelo es temporal discreto.
- **Cuantitativos continuos:** cilindrada, potencia, peso equivalente, economía, emisiones y otras medidas del ensayo.

El tipo de almacenamiento no reemplaza esta clasificación: promediar un código de combustible no tendría una interpretación útil. `Model Year` es constante en 2025 y `FE_UNIT` es constante en MPG.

Hay **11 combustibles o fuentes de energía y 14 procedimientos**. Predominan `Tier 2 Cert Gasoline`, con **3.236 registros**; `Truck`, con **2.030**; y las categorías `FTP` y `HWY`, con **1.577 y 1.340 registros**, respectivamente. Estas frecuencias describen los ensayos incluidos en la base y no el parque automotor. Una misma categoría resumida puede contener procedimientos diferentes.

### 1.4. Valores nulos y su contexto

**Referencia en la notebook:** sección 1.4.

Se calcularon la cantidad y el porcentaje de nulos por atributo. Los faltantes no se interpretan automáticamente como errores: algunas variables solo corresponden a ciertos tipos de ensayo o métodos. Un cero numérico se mantiene como valor y se distingue de una ausencia.

Las cuatro variables ADFE tienen **4.075 nulos cada una —95,05% de los registros—**, coincidentes con `Analytically Derived FE? = No`. Los **212 registros** con `Yes` tienen esos campos completos. El patrón es consistente con variables que se utilizan cuando la economía se deriva analíticamente.

En cilindros hay **670 nulos**: **654** en registros con `Electricity`, **10** con `Hydrogen 5` y **6** con gasolina. La distribución es compatible con diferencias de aplicabilidad, pero no explica cada caso individual. Los seis registros de gasolina requieren una revisión específica.

La economía `RND_ADJ_FE` presenta **221 nulos —5,16%—**. La cantidad de valores disponibles debe tenerse en cuenta al interpretar sus estadísticas. En esta etapa no se imputaron valores ni se eliminaron filas por sus ausencias.

### 1.5. Distribuciones y estadística descriptiva

**Referencia en la notebook:** sección 1.5.

El análisis se concentra en **cilindrada, potencia, cilindros o rotores, marchas, peso equivalente y economía de combustible**. Se utilizaron estadísticas descriptivas e histogramas para observar el centro, la dispersión y los extremos.

| Variable | Resultados globales |
| --- | --- |
| Peso equivalente | Entre 2.750 y 9.000 lb; mediana de 4.750 lb. |
| Potencia nominal | Entre 1 y 1.948 HP; mediana de 305 HP. |
| Cilindrada | Mediana de 2,487 L y máximo de 99,999 L. |
| Economía | Mediana de 32,9 MPG y media aproximada de 65,0 MPG; máximo cercano a 10.000. |

Los resúmenes globales mezclan combustibles y procedimientos distintos. La media de economía es sensible a los valores muy altos y la cilindrada también presenta extremos que afectan su interpretación. Que todas las filas declaren MPG no basta para comparar sin contexto ensayos eléctricos y de gasolina.

Para observar un grupo con combustible y procedimiento comunes se seleccionaron **922 registros** de `Tier 2 Cert Gasoline` y `Federal fuel 2-day exhaust (w/can load)`. Su economía tiene **media de 29,734 MPG, mediana de 26,6 MPG, Q1 de 22,5 MPG, Q3 de 33,475 MPG y máximo de 82,8 MPG**. La media supera a la mediana y el histograma muestra una cola hacia valores altos.

Esta selección permite describir un contexto más específico; no convierte los registros en configuraciones independientes ni representa todos los ensayos urbanos de la base.

### 1.6. Valores extremos y otras particularidades

**Referencia en la notebook:** sección 1.6.

Se inspeccionaron extremos y diagramas de caja junto con el contexto de los registros. Se utiliza el criterio convencional del rango intercuartílico, **RIC = Q3 − Q1**: los valores menores que **Q1 − 1,5 × RIC** o mayores que **Q3 + 1,5 × RIC** se señalan como candidatos a valores atípicos. El criterio describe su posición respecto de la distribución; no demuestra que sean errores ni justifica eliminarlos automáticamente.

En el grupo de gasolina y procedimiento común se identificaron **68 candidatos a valores atípicos**, con límites aproximados de **6,04 y 49,94 MPG**. Se conservaron para su revisión.

Los principales casos identificados para revisar son:

- **95 registros con cilindrada de 99,999 L**, todos asociados a `Electricity`. Podrían responder a una convención de registro, pero su significado exacto no está confirmado.
- **8 registros con economía almacenada como 9999.9999999**, que las tablas redondeadas muestran como 10.000, y otros dos con **4599,1 y 4595,3**. Su interpretación requiere verificación antes de considerarlos eficiencias físicas.
- **2 valores de economía cero y 8 registros con potencia de 1 HP**. Se conservan como valores observados y se distinguen de los nulos.

Estos patrones quedan documentados para la limpieza. No se aplicaron reemplazos ni eliminaciones.

### 1.7. Conclusiones del análisis exploratorio

**Referencia en la notebook:** sección 1.7.

La base contiene 4.287 registros y 1.448 configuraciones, con fuentes de energía y procedimientos diferentes. No hay filas idénticas, pero un número de ensayo puede aparecer varias veces con diferencias en otros atributos. La unidad de análisis deberá definirse antes de continuar.

Los faltantes tienen patrones relacionados con la aplicabilidad de ciertas variables, mientras que otros casos permanecen sin explicar. También se encontraron extremos que afectan los resúmenes globales y cuyo significado requiere revisión. Al fijar combustible y procedimiento, la economía presenta una distribución diferente de la mezcla global, con mediana de 26,6 MPG.

El inciso deja identificadas las decisiones pendientes sobre repeticiones, ausencias, extremos y comparabilidad de registros. La base original se conservó sin correcciones ni imputaciones y todavía no se validaron hipótesis.

## 2. Limpieza de la base

**Estado: pendiente.**

Se documentarán aquí las operaciones que se implementen después del diagnóstico exploratorio. Cada acción deberá indicar el problema que aborda, el criterio utilizado, la cantidad de registros o valores afectados y su justificación. También se explicará cómo se construye la unidad de análisis para las etapas posteriores. Todavía no se definieron ni ejecutaron esas acciones.

## 3. Planteo de hipótesis propias

**Estado: pendiente.**

Se plantearán tres hipótesis de interés, justificadas con información del dominio y con el análisis exploratorio:

- **Hipótesis propia univariada:** pendiente de formular.
- **Hipótesis propia bivariada:** pendiente de formular.
- **Hipótesis propia multivariada:** pendiente de formular.

## 4. Validación de hipótesis

**Estado: pendiente en sus seis apartados.**

Para cada hipótesis se documentarán los datos utilizados, la técnica seleccionada y su justificación, los pasos de evaluación, los resultados y la conclusión correspondiente. Los resultados exploratorios de la sección 1 no constituyen esa validación.

### 4.1. Hipótesis propia univariada

Pendiente de formulación y validación.

### 4.2. Hipótesis propia bivariada

Pendiente de formulación y validación.

### 4.3. Hipótesis propia multivariada

Pendiente de formulación y validación.

### 4.4. Hipótesis del enunciado: economía urbana mínima

**Hipótesis:** la mayoría de las configuraciones de vehículos a combustión alcanzan al menos 25 MPG de economía de combustible en condiciones de conducción urbana.

Pendiente de validación.

### 4.5. Hipótesis del enunciado: economía y tracción

**Hipótesis:** en vehículos de combustión, la economía de combustible difiere según el sistema de tracción del vehículo.

Pendiente de validación.

### 4.6. Hipótesis del enunciado: asociación conjunta de características técnicas

**Hipótesis:** entre vehículos a combustión, las características técnicas del vehículo —peso, potencia, cilindrada, número de cilindros, transmisión y sistema de tracción— se encuentran asociadas conjuntamente con su eficiencia de combustible urbana.

Pendiente de validación.
