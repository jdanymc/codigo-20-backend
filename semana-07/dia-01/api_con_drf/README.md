python3 -m venv venv
source venv/bin/activate
pip install django
pip install djangorestframework
pip install --upgrade pip
pip freeze > requirements.txt
## crear proyecto
```
django-admin startproject codigo
```

## crear aplicación
```
cd codigo
python3 manage.py startapp api
```
## agregar app a settings.py
```
   'api',
   'rest_framework',
```
## migrar por si da error de sesiones
```
python3 manage.py migrate
```
## iniciar servidor
```
python3 manage.py runserver
```
# 
python3 manage.py makemigrations

python3 manage.py migrate