# dataInd/wsgi.py (o dataInd/dataInd/wsgi.py según corresponda a tu estructura local antes de desplegar)
import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Determinar la ruta al directorio raíz del proyecto (/app)
# Si wsgi.py está en /app/dataInd/dataInd/wsgi.py, entonces /app es tres niveles arriba.
# Si wsgi.py está en /app/dataInd/wsgi.py, entonces /app es dos niveles arriba.

# Asumiendo que tu archivo wsgi.py en el repo es dataInd/wsgi.py
# y en el servidor se convierte en /app/dataInd/dataInd/wsgi.py o similar.
# Vamos a ser un poco más genéricos para encontrar la raíz que contiene 'users/' y 'dataInd/'
# Este código asume que 'manage.py' está en la raíz verdadera del proyecto Django
# y que 'users/' está al mismo nivel que el directorio que contiene 'manage.py'.

# Para el caso específico del traceback /app/dataInd/dataInd/wsgi.py:
# Path(__file__) es /app/dataInd/dataInd/wsgi.py
# Path(__file__).resolve().parent es /app/dataInd/dataInd
# Path(__file__).resolve().parent.parent es /app/dataInd
# Path(__file__).resolve().parent.parent.parent es /app/  <-- Aquí debería estar 'users/'
APP_ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Añadir este directorio raíz al sys.path si no está ya
if str(APP_ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(APP_ROOT_DIR))

# Asegúrate de que DJANGO_SETTINGS_MODULE apunte correctamente.
# Si settings.py está en /app/dataInd/dataInd/settings.py,
# y /app/dataInd/ está en sys.path (porque es CWD), entonces 'dataInd.settings' es correcto.
# Si /app/ está en sys.path, entonces 'dataInd.dataInd.settings' sería lo correcto.
# Tu Procfile usa 'dataInd.wsgi', que implica que el CWD de Gunicorn es /app/dataInd/
# y DJANGO_SETTINGS_MODULE es probablemente 'dataInd.settings'.

# La variable de entorno DJANGO_SETTINGS_MODULE suele ser la forma preferida
# de especificar esto, en lugar de fijarlo aquí.
# Pero si necesitas asegurarte, puedes verificar la estructura.
# Por ahora, confiemos en que está bien configurada en Railway o por defecto.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dataInd.settings") # Esta línea es estándar.
                                                                    # El problema es que 'dataInd' (el módulo de settings)
                                                                    # debe ser encontrable, y 'users' también.

application = get_wsgi_application()
