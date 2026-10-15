"""Verifica y ejecuta la notebook desde un kernel nuevo, sin alterar el original."""
from pathlib import Path
import hashlib
import sys
import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parents[1]
requeridos = ['TPE.ipynb', 'informe.md', 'README.md', 'requirements.txt',
              'data/25-testcar-2026-01-21.xlsx']
faltan = [nombre for nombre in requeridos if not (RAIZ / nombre).is_file()]
if faltan:
    raise FileNotFoundError('Faltan archivos requeridos: ' + ', '.join(faltan))
notebooks = [p for p in RAIZ.rglob('*.ipynb')
             if not any(x in p.parts for x in ['.venv', '.ipynb_checkpoints', 'build', '.git'])]
if notebooks != [RAIZ / 'TPE.ipynb']:
    raise ValueError('El proyecto debe contener una única notebook principal: TPE.ipynb')
archivo = RAIZ / 'data/25-testcar-2026-01-21.xlsx'
huella = hashlib.sha256(archivo.read_bytes()).hexdigest()
esperada = 'f131cbb353d0737874e9d61215ba8055b47e4df845f34072bf77faaf780e9dbc'
if huella != esperada:
    raise ValueError('El archivo de datos difiere del original recibido.')
nb = nbformat.read(RAIZ / 'TPE.ipynb', as_version=4)
nbformat.validate(nb)
cliente = NotebookClient(nb, timeout=180, kernel_name='fcd-tpe',
                         resources={'metadata': {'path': str(RAIZ)}})
print('Ejecutando TPE.ipynb desde un kernel nuevo...', flush=True)
cliente.execute()
salida = RAIZ / 'build/TPE_verificado.ipynb'
salida.parent.mkdir(exist_ok=True)
nbformat.write(nb, salida)
pendientes = sum('Pendiente de desarrollo.' in c.source for c in nb.cells)
print(f'Ejecución correcta. Resultado: {salida}')
print(f'Secciones pendientes: {pendientes}. Revisar docs/seguimiento.md antes de entregar.')
