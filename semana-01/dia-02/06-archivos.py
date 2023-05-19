f = open('empresas.txt')
f.write('1010,empresa1,Lima')
f.close()

fr = open('empresas.txt','r')
data_empresas = fr.read()
print(data_empresas)
fr.close()
