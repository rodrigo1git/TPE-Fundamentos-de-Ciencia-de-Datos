# Trabajo Práctico Especial — EPA Fuel Economy 2025

## Estado del trabajo

Este informe presenta el análisis exploratorio inicial del conjunto de datos. La limpieza, el planteo de hipótesis propias y la validación estadística se encuentran pendientes. Los resultados de la sección 1 se reproducen en `TPE.ipynb`, cuyas secciones mantienen la misma numeración que este informe.

## 1. Análisis exploratorio inicial

### 1.1. Contexto y lectura de los datos

**Referencia en la notebook:** sección 1.1, «Contexto y lectura de los datos».

El conjunto EPA Fuel Economy reúne resultados de ensayos de vehículos de año modelo 2025 realizados por la Environmental Protection Agency (EPA) de Estados Unidos y por fabricantes que reportan sus resultados al organismo. Estos ensayos forman parte del proceso de determinación de las estimaciones oficiales de economía de combustible.

Se analizó el archivo `25-testcar-2026-01-21.xlsx`, hoja `Sheet1`. La base combina características de los vehículos —motorización, transmisión, tracción y peso— con las condiciones y los resultados de los ensayos. Contiene **4.287 registros y 67 atributos**.

La economía de combustible indica la distancia recorrida por unidad de combustible. En MPG, un valor mayor representa más millas recorridas por galón y, por lo tanto, mayor eficiencia. El año modelo identifica a los vehículos representados y no equivale a la fecha de realización de cada ensayo. La descripción de la base corresponde a los registros disponibles; no se supone que su composición represente la distribución de vehículos en circulación.

### 1.2. Unidad de observación y repeticiones

**Referencia en la notebook:** sección 1.2, «Unidad de observación y repeticiones».

La combinación de `Veh Mfr Code`, `Test Vehicle ID` y `Test Veh Configuration #` identifica una configuración de vehículo. Con esta clave se reconocen **1.448 configuraciones diferentes**. Una misma configuración puede aparecer en varios ensayos, por lo que la cantidad de filas no debe confundirse con la cantidad de vehículos distintos.

No se encontraron filas completamente idénticas. Sin embargo, existen **4.014 números de ensayo diferentes en 4.287 registros**: `Test Number` no constituye una clave única de la tabla. En las filas que comparten ese identificador se observan diferencias de postratamiento, coeficientes mecánicos o sobremarcha. La causa de esta representación no está confirmada y las filas se conservan durante la exploración.

Estas repeticiones son relevantes para las etapas siguientes: si se calculan estadísticas sobre todas las filas, algunos ensayos reciben más peso que otros. Por ello será necesario definir la unidad de análisis y el tratamiento de las repeticiones antes de realizar inferencias sobre vehículos o configuraciones.

### 1.3. Caracterización de los atributos

**Referencia en la notebook:** sección 1.3, «Caracterización de los 67 atributos», tabla de diccionario y tablas de frecuencias.

Los atributos se organizaron según su significado, escala estadística, unidad, tipo computacional, cantidad de valores distintos y presencia de nulos. Se distinguieron los identificadores de las variables de medición y de las categorías. Los códigos de combustible, transmisión o procedimiento se consideran nominales, aunque algunos estén almacenados como números; promediarlos no tendría una interpretación útil. Cilindros y marchas se tratan como conteos discretos, mientras que las medidas físicas se describen como variables continuas. Las banderas sí/no son nominales dicotómicas.

`Model Year` y `FE_UNIT` tienen un único valor en todos los registros: 2025 y MPG, respectivamente. El factor de ponderación del promediado también tiene un único valor entre los casos informados, pero presenta numerosos nulos; por lo tanto, no tiene la misma cobertura que las otras columnas constantes.

La base incluye **11 combustibles o fuentes de energía y 14 procedimientos de ensayo**. Predomina `Tier 2 Cert Gasoline`, con **3.236 registros**. La categoría de vehículo más frecuente es `Truck`, con **2.030 registros**, y las categorías de ensayo más frecuentes son `FTP`, con **1.577**, y `HWY`, con **1.340**. Estas cantidades describen la composición de los registros disponibles y no las preferencias de los consumidores ni el parque automotor. Asimismo, una categoría resumida de ensayo no identifica necesariamente un único procedimiento.

### 1.4. Valores nulos y su contexto

**Referencia en la notebook:** sección 1.4, «Valores nulos y su contexto», tablas y gráfico de faltantes.

Se calcularon la cantidad y el porcentaje de faltantes por atributo y se examinó su distribución según combustible, categoría de ensayo y método de obtención de resultados. Se mantuvo la diferencia entre un cero numérico y una celda sin dato.

Las cuatro columnas ADFE tienen **4.075 nulos cada una, equivalentes al 95,05% de los registros**. Esas ausencias corresponden a `Analytically Derived FE? = No`; los **212 registros** que informan `Yes` tienen los cuatro campos completos. El patrón es consistente con el carácter condicional de estas variables, asociadas a la economía de combustible derivada analíticamente.

`Averaging Group ID` y `Averaging Weighting Factor` presentan **4.212 nulos**, asociados a `No averaging`. Estas variables corresponden a los casos en que se utiliza un método de promediado. Su elevada proporción de ausencias no constituye, por sí sola, una justificación para descartarlas o completar sus valores.

En cilindros y postratamiento se encontraron **670 nulos**: **654** corresponden a registros con `Electricity`, **10** a `Hydrogen 5` y **6** a gasolina. Esta distribución es compatible con diferencias en la aplicabilidad de los atributos, pero no permite establecer la causa individual de todas las ausencias. Los registros de gasolina requieren una revisión específica.

`RND_ADJ_FE` presenta **221 nulos, un 5,16% del total**. Las medidas por fase o bolsa tienen coberturas diferentes según la categoría de ensayo. En consecuencia, el número de observaciones disponibles debe acompañar la interpretación de cada resumen. No se imputaron valores ni se eliminaron registros por estas ausencias.

### 1.5. Distribuciones y estadística descriptiva

**Referencia en la notebook:** sección 1.5, «Distribuciones y estadística descriptiva», tablas de resumen, histogramas y diagrama de caja.

Se calcularon medidas de posición, dispersión y forma para las variables cuantitativas, excluyendo códigos e identificadores. Los histogramas complementan los resúmenes numéricos y permiten observar colas, concentraciones y valores alejados. Los resultados globales describen una mezcla de fuentes de energía y procedimientos, por lo que no deben interpretarse como si todos los registros fueran homogéneos.

Entre las características principales se observaron los siguientes valores:

| Variable | Resultados globales |
| --- | --- |
| Peso equivalente de ensayo | Entre 2.750 y 9.000 lb; mediana de 4.750 lb. |
| Potencia nominal | Entre 1 y 1.948 HP; mediana de 305 HP. |
| Cilindrada | Mediana de 2,487 L y máximo de 99,999 L. |
| Economía de combustible | Mediana de 32,9 MPG y media aproximada de 65,0 MPG; máximo cercano a 10.000. |

La diferencia entre la media y la mediana de economía, junto con los extremos observados, muestra que la media global requiere cautela. La misma precaución se aplica a la cilindrada: los valores de 99,999 L asociados a registros eléctricos afectan su resumen. El uso de una unidad declarada común tampoco basta para interpretar un ensayo eléctrico como si fuera uno de gasolina.

Para describir un grupo con combustible y procedimiento comunes se seleccionaron los registros de `Tier 2 Cert Gasoline` y `Federal fuel 2-day exhaust (w/can load)`. Esta vista contiene **922 registros** y presenta:

| Medida de economía | Valor |
| --- | ---: |
| Media | 29,734 MPG |
| Mediana | 26,6 MPG |
| Primer cuartil | 22,5 MPG |
| Tercer cuartil | 33,475 MPG |
| Máximo | 82,8 MPG |

La media supera a la mediana y el histograma presenta una cola hacia valores altos. La comparación con el resumen global muestra cómo cambia la descripción al fijar combustible y procedimiento. Esta selección no garantiza independencia entre los registros ni representa, por sí sola, todos los ensayos urbanos de la base.

En varias distribuciones de emisiones y medidas por bolsa se observan concentraciones en los valores bajos y colas hacia valores mayores. Su cobertura desigual impide compararlas como si tuvieran el mismo tamaño de muestra. Las variables ADFE describen únicamente sus 212 registros aplicables. También se observaron valores negativos en algunos coeficientes mecánicos: su signo no permite declararlos inválidos sin considerar la definición técnica correspondiente.

### 1.6. Valores extremos y otras particularidades

**Referencia en la notebook:** sección 1.6, «Valores extremos y otras particularidades», tabla de percentiles y registros seleccionados para revisión.

Se inspeccionaron mínimos, máximos y observaciones de las colas junto con el contexto de cada fila. Los percentiles 1 y 99 se utilizaron como referencias para examinar esas colas, sin considerarlos límites de validez. El diagrama de caja de la sección anterior utiliza bigotes mínimo–máximo; no clasifica automáticamente observaciones como outliers.

Los principales casos identificados para revisar son:

- **95 registros con cilindrada de 99,999 L**, todos asociados a `Electricity`. El patrón podría responder a una convención de registro, pero su significado exacto no está confirmado.
- **8 registros con `RND_ADJ_FE` almacenado como 9999.9999999**, que las tablas redondeadas muestran como 10.000; también se encontraron valores de **4599,1 y 4595,3**. Su interpretación debe verificarse antes de tratarlos como eficiencias físicas.
- **2 registros con economía igual a cero** y **8 con potencia de 1 HP**. Se conservan como valores observados y no se equiparan automáticamente a nulos.
- Valores de **PM próximos a 10.000 g/mi** y máximos alejados del resto en algunos coeficientes mecánicos. Son señales adicionales para inspeccionar con el contexto de las filas.

Un valor extremo no demuestra por sí solo un error. Las posibles explicaciones incluyen convenciones de registro, resultados del procedimiento de cálculo o inconsistencias; el diagnóstico actual no permite elegir una explicación para todos los casos. No se realizaron reemplazos ni eliminaciones.

### 1.7. Relaciones descriptivas

**Referencia en la notebook:** sección 1.7, «Relaciones descriptivas», matriz de Pearson, tabla de pares disponibles y gráficos de dispersión.

Se exploraron relaciones entre economía de combustible y características técnicas dentro del mismo grupo de gasolina Tier 2 y procedimiento federal de dos días utilizado en la sección 1.5. Se calcularon correlaciones de Pearson por pares disponibles y se acompañaron con sus tamaños de muestra y gráficos de dispersión.

La economía presenta asociaciones lineales negativas con la potencia (**r ≈ −0,659**), la cilindrada (**r ≈ −0,539**) y el peso equivalente (**r ≈ −0,479**). En este grupo, los valores mayores de esas características tienden a acompañarse de economías menores, aunque existe dispersión alrededor de las tendencias. La potencia y la cilindrada se asocian positivamente entre sí (**r ≈ 0,755**).

Estos coeficientes describen asociaciones lineales y no demuestran causalidad. Las repeticiones de ensayos y configuraciones permanecen en la vista, de modo que los resultados corresponden a las filas analizadas y no a una muestra independiente de vehículos. No se realizaron pruebas de significación ni se consideraron validadas las hipótesis de las etapas siguientes.

### 1.8. Conclusiones del análisis exploratorio

**Referencia en la notebook:** sección 1.8, «Conclusiones del inciso 1».

La base combina 4.287 registros, 67 atributos y 1.448 configuraciones de año modelo 2025. Incluye procedimientos y fuentes de energía diferentes, con predominio de gasolina Tier 2. La multiplicidad de ensayos por configuración y la repetición de números de ensayo hacen necesario definir cuidadosamente la unidad de análisis antes de avanzar.

Los faltantes más frecuentes se relacionan con métodos que solo se aplican a ciertos registros, como ADFE y promediado. Otras ausencias, en particular las de economía y emisiones, deben examinarse según procedimiento y combustible. La cobertura de cada variable es parte de la interpretación de sus estadísticas.

Las distribuciones globales contienen extremos que afectan los resúmenes, entre ellos cilindradas de 99,999 L en registros eléctricos y economías cercanas a 10.000. Su significado queda pendiente de verificación. Dentro del grupo de gasolina y procedimiento común se obtuvo una mediana de economía de 26,6 MPG y asociaciones negativas con potencia, cilindrada y peso; estos resultados son descriptivos.

El análisis deja identificados los aspectos que deberán tratarse en la limpieza: granularidad y repeticiones, ausencias condicionales y no explicadas, valores extremos y selección de registros comparables. La base original se conservó sin correcciones ni imputaciones.

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
