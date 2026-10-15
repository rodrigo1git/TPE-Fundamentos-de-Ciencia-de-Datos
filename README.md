# TPE – Fundamentos de la Ciencia de Datos

Análisis de EPA Fuel Economy, año modelo 2025.

## Organización

```text
TPE.ipynb                 Notebook principal: incisos 1 a 4
informe.md                Informe con referencias a las secciones de la notebook
data/
  25-testcar-2026-01-21.xlsx
docs/
  enunciado.pdf
  seguimiento.md          Estado de avance y control de la entrega
requirements.in           Dependencias directas del proyecto
requirements.txt          Versiones instaladas para reconstruir el entorno
scripts/
  verificar.py            Comprobación y ejecución completa desde un kernel nuevo
```

Se mantiene una única notebook de trabajo. El Excel en `data/` es el original y no se sobrescribe con datos limpiados. Las secciones del informe siguen la numeración de la notebook.

## Preparación del entorno

Entorno comprobado: Python 3.12, macOS con Apple Silicon. Se recomienda Python 3.12 para reconstruirlo; otras plataformas no fueron verificadas.

Desde una terminal, clonar y entrar al repositorio:

```bash
git clone https://github.com/rodrigo1git/TPE-Fundamentos-de-Ciencia-de-Datos.git
cd TPE-Fundamentos-de-Ciencia-de-Datos
```

En macOS o Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --prefix "$VIRTUAL_ENV" --name fcd-tpe --display-name "Python (FCD - TPE)"
python -m jupyterlab
```

En Windows PowerShell, con Python 3.12 instalado:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --prefix .venv --name fcd-tpe --display-name "Python (FCD - TPE)"
.\.venv\Scripts\python.exe -m jupyterlab
```

Abrir `TPE.ipynb` y seleccionar **Python (FCD - TPE)**. Iniciar Jupyter siempre desde la raíz del proyecto para que las rutas relativas a `data/` funcionen.

## Continuar el trabajo

1. Desarrollar el siguiente inciso en su sección de `TPE.ipynb` y conservar las etapas anteriores reproducibles.
2. Mantener `datos` como base original. Al implementar limpieza, generar una copia para los análisis posteriores y documentar sus cambios.
3. Actualizar los hallazgos y conclusiones en la sección correspondiente de `informe.md`.
4. Registrar el avance en `docs/seguimiento.md` y guardar la notebook con sus resultados.
5. Antes de modificar la notebook, coordinar quién la edita para evitar conflictos. Usar GitHub para versionar y empaquetar la entrega.

Si se agrega una dependencia, incorporarla a `requirements.in` y actualizar las versiones de `requirements.txt` después de verificar el entorno. No subir `.venv/` ni copiar código de pruebas descartadas a la notebook principal.

Para publicar un avance revisado, desde la raíz del proyecto:

```bash
git status
git add README.md .gitignore TPE.ipynb informe.md data docs requirements.in requirements.txt scripts
git commit -m "Actualizar trabajo práctico"
git push origin main
```

El usuario que publica debe tener permiso de escritura en el repositorio.

## Verificación

Con el entorno activado, desde la raíz:

```bash
python -m pip check
python scripts/verificar.py
```

En Windows se puede utilizar `.\.venv\Scripts\python.exe` en lugar de `python` sin activar el entorno.

El verificador comprueba los archivos requeridos, la integridad del Excel y el formato de la notebook; luego ejecuta todas las celdas en un kernel nuevo y guarda el resultado en `build/TPE_verificado.ipynb`. La copia de comprobación está excluida de Git. Una ejecución correcta certifica el código desarrollado, pero no que estén completos los incisos pendientes.

## Entrega

La entrega debe incluir la notebook completa y ejecutable, el informe, el archivo de datos, `requirements.txt` y este README. Antes de compartir el enlace, completar la revisión de `docs/seguimiento.md` y comprobar que los archivos estén efectivamente en el repositorio remoto.

Fecha indicada en el enunciado: **10 de noviembre de 2026, 23:59**. Devolución inicial: 17 de noviembre. Defensa oral: semana del 23 al 27 de noviembre, a coordinar con el ayudante.
