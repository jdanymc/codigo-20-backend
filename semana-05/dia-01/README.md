# Django

## Creamos el entorno virtual
````
python3 -m venv venv
````
## Activamos el entorno virtual
````
source venv/bin/activate
````

## Instalar django
````
pip install django
````
## Crear proyecto de ejemplo

````
django-admin startproject ejemplo
`````

## Correr el servidor

````
cd ejemplo
python3 manage.py runserver
````

## Migraciones de la base de datos

````
python3 manage.py migrate  
````

## Mostrar tablas migradas

````
python3 manage.py showmigrations
````

## Crear un super usuario
````
python3 manage.py createsuperuser
````
{usuario: admin, password: admin}