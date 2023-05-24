## Para crear un entorno virtual con python3
```
python -m venv nombre_entorno (ej. venv)
```
## Para activar el entorno virtual
```
# Windows
nombre_entorno\Scripts\activate

# Linux o Mac
source nombre_entorno/bin/activate
```

## Para desactivar el entorno virtual
```
deactivate
```

## Para instalar dependencias
```
pip install nombre_paquete (ej. pip install django)
```

## Para crear un archivo con las dependencias
```
pip freeze > requirements.txt
```

## Para instalar las dependencias (despues de activar el entorno virtual)
```
pip install -r requirements.txt
```
