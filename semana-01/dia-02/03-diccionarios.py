capitales = {
    'Peru': 'Lima',
    'Ecuador': 'Quito',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Argentina': 'Buenos Aires',
}

print(capitales)
print(capitales['Peru'])

nuevaCapital = {
    'Brasil': 'Brasilia'
}

capitales.update(nuevaCapital)

print(capitales)
'''
pais = input('Ingrese el país: ')
capital = capitales.get(pais)
print('la capital de ' + pais + ' es ' + capital)'''

capitales.update({'Chile': 'Arica'})
print(capitales)
capitales.pop('Chile')
print(capitales)

# pais = input('Ingrese el país a eliminar : ')
# capitalEliminada = capitales.pop(pais,'no existe')
# print("capital eliminada : " + capitalEliminada)
# print(capitales)

#recorrer diccionarios
#recorrer claves
print('paises : ')
print('*'*20)
for clave in capitales.keys():
    print(clave)

#recorrer valores

print('*'*20)
print('capitales : ')
print('*'*20)
for valor in capitales.values():
    print(valor)
print('*'*20)

#recorrer claves y valores

for clave, valor in capitales.items():
    print('la capital de '+clave + ' es ' + valor)    