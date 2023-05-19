'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if(numero%2==0):
        pares.append(numero)

print(pares)
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)
pares = []
for num in numeros:
    if(num%2==0):
        pares.append(num)

print(pares)

# usando list comprehentions
impares = [num for num in numeros if num%2!=0]

print(impares)

paises = ['Peru', 'Ecuador', 'Chile', 'Uruguay', 'Argentina']
paises_minusculas = [pais.lower() for pais in paises]

print(paises)
print(paises_minusculas)

numeros = [num for num in range(50)]
print(numeros)

numeros = [num for num in range(1,101,1) if num%2==0]
print(numeros)
