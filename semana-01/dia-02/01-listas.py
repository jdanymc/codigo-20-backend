dias = ['lunes', 'martes', 'miércoles']
print(dias)
print(dias[0])
print(dias[0:2])

#agregar valor a una lista

dias.append('jueves')

print(dias)

dias.append(5)

print(dias)

#eliminar valor de una lista

dias.pop(1)
print(dias)

del dias[1:3]
print(dias)

#actualizar valor de una lista
dias[1]='martes'
print(dias)

#recorrer una lista
print('fors : ')
for contador in range(len(dias)):
    print(dias[contador])

for dia in dias:
    print(dia)  