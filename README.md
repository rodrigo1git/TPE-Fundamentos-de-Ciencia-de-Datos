# TPE — Fundamentos de Ciencias de Datos

## Descripción

Análisis del conjunto de datos EPA Fuel Economy: exploración de los datos, limpieza, formulación de hipótesis y evaluación mediante pruebas estadísticas y modelos. El desarrollo y las conclusiones de cada análisis se encuentran en `TPE.ipynb`.

## Archivos principales

- `TPE.ipynb`: notebook con el desarrollo completo.
- `data/25-testcar-2026-01-21.xlsx`: datos utilizados, en la hoja `Sheet1`.
- [Informe_TPE_Grupo_13.pdf](Informe_TPE_Grupo_13.pdf): informe con los principales resultados y conclusiones.
- `requirements.txt`: dependencias para ejecutar el notebook.

## Instalación

Se recomienda **Python 3.12**, versión con la que se comprobó la ejecución. Descargar el repositorio y abrir una terminal en su carpeta principal, donde están `TPE.ipynb` y `requirements.txt`.

Crear y activar un entorno virtual:

**macOS / Linux**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

**Windows (Símbolo del sistema / CMD)**

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Con el entorno activado, instalar las dependencias y registrar el kernel:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name tpe-grupo13 --display-name "Python (TPE Grupo 13)"
```

## Ejecución

1. Desde la carpeta principal del proyecto y con el entorno activado, iniciar JupyterLab:

   ```bash
   python -m jupyterlab
   ```

2. Abrir `TPE.ipynb` y seleccionar el kernel **Python (TPE Grupo 13)**.
3. Elegir **Kernel → Restart Kernel and Run All Cells…** para ejecutar todas las celdas desde el inicio.
4. Esperar a que termine la ejecución para consultar las tablas, los gráficos y los resultados de las hipótesis.

Las celdas deben ejecutarse en orden, porque los análisis usan los datos preparados en los puntos anteriores. Mantener el archivo Excel dentro de `data/`, con su nombre original: el notebook lo lee mediante una ruta relativa y no necesita descargar datos adicionales.
