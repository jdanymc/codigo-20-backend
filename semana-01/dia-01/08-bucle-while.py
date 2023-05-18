contador = 1
while (contador <= 3):
    print(contador)
    contador+=1

continuar='si'
resultado = 0
while(continuar=='si'):
    numero = int(input("ingrese un numero: "))
    resultado += numero
    continuar = input("Desea ingresar mas numeros: ")

print(resultado)