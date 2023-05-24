def dividir(dividendo, divisor):
    return dividendo / divisor

#resultado = dividir(10,5)
#print(resultado)

if __name__ == "__main__":
    try:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))
        resultado = dividir(dividendo,divisor)
        if resultado == 5:
            raise Exception("El resultado no deberia ser 5")
        print('resultado: ',resultado)
   # except ValueError as a:
   #     print("Solo se acepta numeros enteros, ",a)
   # except ZeroDivisionError as b:
   #     print("No se puede dividir por cero, ",b)
    except Exception as c:
        print("Ocurrió un error, ",c)
    finally:
        print("Se ha finalizado el proceso")   
