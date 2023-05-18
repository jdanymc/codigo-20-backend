palabra = input("Ingrese una palabra: ")
divisor = int(input("Ingrese un divisor: "))

grupo = len(palabra)/divisor
while (grupo > 0):
    print(palabra[:divisor])
    palabra = palabra[divisor:]
    grupo -= 1