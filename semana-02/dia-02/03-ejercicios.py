# ejercicio: invertir una oración
# input: "Hola como estas"
# output: "estas como Hola"

def solucion(sentencia:str):
    nueva_sentencia = sentencia.split(' ')[::-1]
    #resultado = ' '.join(nueva_sentencia)
    for palabra in nueva_sentencia:
        resultado += palabra + ' '
    return resultado.strip()

if __name__ == "__main__":
    sentencia = input("Ingrese una oración: ")
    resultado = solucion(sentencia)
    print(resultado)