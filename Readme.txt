Pasos para la creación
python -m venv env

activacion
.\env\Scripts\activate
Mac source env/bin/activate

pip install django

django-admin startproject nombre_del_proyecto

si se quiere configurar con PostgreSQL se ingresa al archivo  settings.py y se configura de la siguiente manera

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_la_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Seguridad:
Asegúrate de tener una clave secreta (ya generada automáticamente) y de que DEBUG esté en True solo durante el desarrollo.

4. Migraciones Iniciales

python manage.py migrate

5. Creación de una Aplicación Django

python manage.py startapp nombre_de_la_aplicacion

Luego, agrega esta aplicación a la lista de INSTALLED_APPS en el archivo settings.py:
INSTALLED_APPS = [
    ...
    'nombre_de_la_aplicacion',
]



en la carpeta raíz 
pip freeze > requirements.txt

pip install -r requirements.txt

para desactivar se coloca deactivate en la terminal y ya 
deactivate




Para revisar 

un nuevo modelo y un nuevo campo en en el modelo de indicadores 
para agregar periodicidad 
 posteriormente en rewsultados agregar el nombre de la sede 
crear un nuivo modelos de sedes 