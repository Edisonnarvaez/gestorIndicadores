# En tu archivo local: dataInd/wsgi.py
import os
import sys
from pathlib import Path
import logging # Importar logging
from django.core.wsgi import get_wsgi_application # Mover la importación aquí

# Configurar logging básico para ver la salida en los logs de Railway
# (Railway debería capturar la salida estándar)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("--- INICIO SCRIPT WSGI ---")
logger.info(f"Directorio de trabajo actual (CWD): {os.getcwd()}")
logger.info(f"Contenido de sys.path INICIAL: {sys.path}")

# Asumimos que este archivo (wsgi.py) en tu repo está en 'dataInd/wsgi.py'
# y que 'users/' es un directorio hermano de 'dataInd/'
# Ejemplo de estructura en tu repo:
# ./manage.py
# ./dataInd/ (contiene este wsgi.py, settings.py)
# ./users/ (tu app)

# Ruta al archivo wsgi.py actual
wsgi_file_path = Path(__file__).resolve()
logger.info(f"Ubicación de wsgi.py: {wsgi_file_path}")

# El traceback dice que wsgi.py está en /app/dataInd/dataInd/wsgi.py en el servidor.
# Si esa es la ubicación de ESTE archivo en el servidor:
# - wsgi_file_path.parent es /app/dataInd/dataInd/
# - wsgi_file_path.parent.parent es /app/dataInd/
# - wsgi_file_path.parent.parent.parent es /app/

# Supongamos que la raíz de tu proyecto (donde está manage.py y donde users/ debería ser un subdir)
# termina siendo /app/dataInd/ en el servidor, si todo tu repo se copia dentro de /app/dataInd/
# O, si tu repo se copia en /app/, entonces la raíz es /app/

# Vamos a verificar la estructura más probable basada en el traceback:
# Si wsgi.py es /app/dataInd/dataInd/wsgi.py, entonces settings.py está en el mismo dir.
# Y 'users' app (como está en el repo: hermana de 'dataInd' proyecto) estaría en /app/dataInd/users/
# (si todo el repo se copia en /app/dataInd/)
# O en /app/users/ (si todo el repo se copia en /app/)

# Hipótesis 1: Todo tu repo se copia en /app/dataInd/ en el servidor.
# Entonces, el CWD (que parece ser /app/dataInd/) sería la raíz efectiva para encontrar 'users'.
# En este caso, '/app/dataInd/users/' debería existir.
server_repo_root_h1 = wsgi_file_path.parent.parent # Esto sería /app/dataInd/
logger.info(f"Hipotética raíz del repo en servidor (H1 - /app/dataInd/): {server_repo_root_h1}")
logger.info(f"Contenido de {server_repo_root_h1} (ls -a):")
try:
    for item in server_repo_root_h1.iterdir():
        logger.info(f"  H1 - {item.name} {'(dir)' if item.is_dir() else '(file)'}")
except Exception as e:
    logger.info(f"  H1 - Error listando contenido de {server_repo_root_h1}: {e}")

expected_users_path_h1 = server_repo_root_h1 / "users"
logger.info(f"Ruta esperada para 'users' (H1): {expected_users_path_h1}")
logger.info(f"¿Existe {expected_users_path_h1}? {expected_users_path_h1.exists()}")
if expected_users_path_h1.exists():
    logger.info(f"Contenido de {expected_users_path_h1} (ls -a):")
    try:
        for item in expected_users_path_h1.iterdir():
            logger.info(f"  H1 users - {item.name} {'(dir)' if item.is_dir() else '(file)'}")
    except Exception as e:
        logger.info(f"  H1 users - Error listando contenido: {e}")


# Hipótesis 2: Todo tu repo se copia en /app/ en el servidor.
# Entonces, '/app/users/' debería existir.
server_repo_root_h2 = wsgi_file_path.parent.parent.parent # Esto sería /app/
logger.info(f"Hipotética raíz del repo en servidor (H2 - /app/): {server_repo_root_h2}")
logger.info(f"Contenido de {server_repo_root_h2} (ls -a):")
try:
    for item in server_repo_root_h2.iterdir():
        logger.info(f"  H2 - {item.name} {'(dir)' if item.is_dir() else '(file)'}")
except Exception as e:
    logger.info(f"  H2 - Error listando contenido de {server_repo_root_h2}: {e}")

expected_users_path_h2 = server_repo_root_h2 / "users"
logger.info(f"Ruta esperada para 'users' (H2): {expected_users_path_h2}")
logger.info(f"¿Existe {expected_users_path_h2}? {expected_users_path_h2.exists()}")
if expected_users_path_h2.exists():
    logger.info(f"Contenido de {expected_users_path_h2} (ls -a):")
    try:
        for item in expected_users_path_h2.iterdir():
            logger.info(f"  H2 users - {item.name} {'(dir)' if item.is_dir() else '(file)'}")
    except Exception as e:
        logger.info(f"  H2 users - Error listando contenido: {e}")

# Añadir la ruta que *debería* contener 'users' si la Hipótesis 1 es correcta y CWD es la raíz del repo
# (CWD suele estar en sys.path por defecto)
# Si la H1 es correcta, CWD (/app/dataInd/) ya estaría en sys.path.
# Si la H2 es correcta (/app/ es la raíz), entonces /app/ debería estar en sys.path.
# La modificación de sys.path que intentaste antes era para la H2.
if server_repo_root_h2.exists() and str(server_repo_root_h2) not in sys.path:
    sys.path.insert(0, str(server_repo_root_h2))
    logger.info(f"Añadido a sys.path (H2): {server_repo_root_h2}")
    logger.info(f"Contenido de sys.path DESPUÉS de añadir H2: {sys.path}")


# Esta variable de entorno es crucial.
# Si DJANGO_SETTINGS_MODULE es "dataInd.settings":
# Y el CWD es /app/dataInd/ (que está en sys.path), buscará /app/dataInd/dataInd/settings.py
# Y esto es consistente con el traceback /app/dataInd/dataInd/wsgi.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dataInd.settings")
logger.info(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

logger.info("--- ANTES DE LLAMAR a get_wsgi_application ---")
application = get_wsgi_application() # Esta es la línea 43 en tu último traceback
logger.info("--- DESPUÉS DE LLAMAR a get_wsgi_application (si no hay error antes) ---")
