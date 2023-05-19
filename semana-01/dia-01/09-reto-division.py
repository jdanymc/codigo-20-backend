#ENTRADA
texto = input("Ingrese un texto: ")
divisor = int(input("Ingrese un divisor: "))

#PROCESO
'''
grupo = len(texto)/divisor
while (grupo > 0):
    print(texto[:divisor])
    texto = texto[divisor:]
    grupo -= 1
'''
#['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for contador in range(0,len(texto),divisor):
    salida = texto[contador:contador+divisor]
    print(salida)
