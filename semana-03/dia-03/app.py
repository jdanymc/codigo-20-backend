from flask import Flask, request
#from mysql import connector
import mysql.connector
import psycopg2
from markupsafe import escape

app=Flask(__name__)

#app.config['']
mysql_db = mysql.connector.connect(host="localhost",user="root",password="123456.a",database="codigo")
postgres_db = psycopg2.connect(host="localhost",user="postgres",password="123456",database="codigo", port="5432")
mysql_cursor = mysql_db.cursor()
postgres_cursor = postgres_db.cursor()


@app.route('/')
def index():
    return "La API funciona correctamente"

@app.route('/mysql/registrar-alumno', methods=['POST','GET'])
def registrar_alumno_mysql():
    method = request.method
    if method == 'GET':
        try:
            sql='SELECT * FROM codigo.alumnos'
            mysql_cursor.execute(sql)
            record = mysql_cursor.fetchall()
            mysql_db.close()
            response = []
            for alumno in record:
                response.append({
                    'id': alumno[0],
                    'nombre': alumno[1],
                    'apellido': alumno[2]
                })
            return response, 200
        except Exception as e:
             return {
                'message':'Error',
                'error': str(e)
            },400
    else:
        try:
            json = request.get_json()
            sql = 'INSERT INTO codigo.alumnos (nombre, apellido) VALUES (%s, %s)'
            secure_sql = escape(sql) 
            values = (json['nombre'],json['apellido'])
            mysql_cursor.execute(secure_sql, values)
            mysql_db.commit()
            mysql_db.close()
            
            return {
                'message':'Alumno registrado correctamente',
            },200
        except Exception as e:
            return {
                'message':'Error',
                'error': str(e)
            },400
        
@app.route('/postgres/registrar-alumno', methods=['POST','GET'])
def registrar_alumno_postgres():
    method = request.method
    if method == 'GET':
        try:
            sql='SELECT * FROM public.alumnos'
            postgres_cursor.execute(sql)
            record = postgres_cursor.fetchall()
            postgres_db.close()
            response = []
            for alumno in record:
                response.append({
                    'id': alumno[0],
                    'nombre': alumno[1],
                    'apellido': alumno[2]
                })
            return response, 200
        except Exception as e:
            return {
                'message':'Error',
                'error': str(e)
            },400    
    else:
        try:
            json = request.get_json()
            sql = 'INSERT INTO public.alumnos (nombre, apellido) VALUES (%s, %s)'
            secure_sql = escape(sql) 
            values = (json['nombre'],json['apellido'])
        
            postgres_cursor.execute(secure_sql, values)
            postgres_db.commit()
            postgres_db.close()

            return {
                'message':'Alumno registrado correctamente',
            },200

        except Exception as e:
            return {
                'message':'Error',
                'error': str(e)
            },400
        
if __name__ == '__main__':
    app.run(debug=True)