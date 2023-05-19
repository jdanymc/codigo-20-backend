#la tupla es inmutable
dias = ("lunes", "martes", "miércoles","jueves","viernes")

print(dias)

dias = list(dias)
dias.append("sábado")
dias = tuple(dias)

print(dias)

for dia in dias:
    print(dia)