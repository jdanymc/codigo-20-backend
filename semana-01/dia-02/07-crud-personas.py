    # persona {dni, nombre, email}
    
import os
import time

"""
CRUD
C = CREATE
R = READ
U = UPDATE
D = DELETE
"""
persona = {
    'dni':'11111111',
    'nombre':'nombre 1',
    'email':'mail1@email.com'
}
lista_personas = []
opcion = 0
ANCHO = 50

################ FUNCIONES ##################
def buscar_persona(valor_busqueda):
    posicion_busqueda = -1
    for posicion in range(len(lista_personas)):
            dic_persona = lista_personas[posicion]
            for clave,valor in dic_persona.items():
                if(clave=="dni" and valor== valor_busqueda):
                    posicion_busqueda = posicion
                    break
    return posicion_busqueda

def grabar_datos():
    str_datos = ""
    for dic_empresa in lista_personas:
        str_datos += dic_empresa.get("dni") + ","
        str_datos += dic_empresa.get("nombre") + ","
        str_datos += dic_empresa.get("email") + "\n"
    return str_datos

def cargar_datos(str_datos):
    lista_datos = []
    listado_general = str_datos.splitlines()
    for str_registro in listado_general:
        lista_registro = str_registro.split(',')
        dic_registro = {
            'dni':lista_registro[0],
            'nombre':lista_registro[1],
            'email':lista_registro[2]
        }
        lista_datos.append(dic_registro)
    return lista_datos
    
    
            

#############################################

#arch = Path('personas.csv')
#arch.touch(exist_ok=True)
f = open('personas.csv','a+')
str_datos = f.read()
f.close()

lista_personas = cargar_datos(str_datos)

while(opcion != 5):
    #time.sleep(1)
    print("="*ANCHO)
    print(" "*int(ANCHO/5) + "REGISTRO DE PERSONAS")
    print("="*ANCHO)
    print("""
          [1] REGISTRAR PERSONA
          [2] LISTADO DE PERSONAS
          [3] ACTUALIZAR PERSONA
          [4] ELIMINAR PERSONA
          [5] SALIR DEL PROGRAMA
          """)
    print("="*ANCHO)
    opcion = int(input("INGRESE UNA OPCIÓN DEL MENU :"))    
    os.system("clear")
    
    if(opcion == 1):
        print("[1] REGISTRO DE NUEVA PERSONA")
        dni = input("DNI : ")
        nombre = input("NOMBRE : ")
        email = input("EMAIL : ")
        dic_nueva_persona = {
            'dni':dni,
            'nombre':nombre,
            'email':email
        }
        lista_personas.append(dic_nueva_persona)
    elif(opcion==2):
        print("[2] RELACIÓN DE PERSONAS")
        for dic_persona in lista_personas:
            print('*'*ANCHO)
            for clave,valor in dic_persona.items():
                print(clave + " : " + valor)
            print('*'*ANCHO)
        input("presione ENTER para continuar...")
    elif(opcion==3):
        print("[3] ACTUALIZAR PERSONAS")
        valor_busqueda = input('INGRESE DNI:')
        posicion_busqueda = buscar_persona(valor_busqueda)
        if(posicion_busqueda == -1):
            print(" NO SE ENCONTRO PERSONA")
        else:
            dic_persona_busqueda = lista_personas[posicion_busqueda]
            print("PERSONA ENCONTRADA : " + dic_persona_busqueda.get('nombre'))
            nombre = input("NOMBRE : ")
            email = input("EMAIL : ")
            dic_persona_actualizar = {
                'dni':dic_persona_busqueda.get('dni'),
                'nombre':nombre,
                'email':email
            }
            lista_personas[posicion_busqueda] = dic_persona_actualizar
            print("PERSONA ACTUALIZADA")
            
    elif(opcion==4):
        print("[4] ELIMINAR UNA PERSONA")
        valor_busqueda = input('INGRESE DNI:')
        posicion_busqueda = posicion_busqueda = buscar_persona(valor_busqueda)
                
        if(posicion_busqueda == -1):
            print(" NO SE ENCONTRO PERSONA")
        else:
            lista_personas.pop(posicion_busqueda)
            print(" PERSONA ELIMINADA !!!")
    elif(opcion==5):
        fsalida = open('personas.csv','w+')
        fsalida.write(grabar_datos())
        fsalida.close()
        
        print("[5] ESTA SALIENDO DEL PROGRAMA")
    else:
        print("OPIÓN NO VALIDA!!!")
    
    
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    
