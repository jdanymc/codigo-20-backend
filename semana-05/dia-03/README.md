## Imicializar web app
`````
python3 manage.py startapp web  
`````

## Arrancar proyecto
`````
python3 manage.py runserver   
`````

## Migrar modelo
`````
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py sqlmigrate web 0001
python3 manage.py migrate
`````

## Crear usuario {admin:admin}
`````
python3 manage.py createsuperuser
`````