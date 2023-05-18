fraseInicial = input("Ingrese una frase: ")
fraseInicial = fraseInicial.lower().replace(' ','')
fraseReversa = fraseInicial[::-1]

if(fraseInicial == fraseReversa):
    print("Es palindromo")
else:
    print("No es palindromo")