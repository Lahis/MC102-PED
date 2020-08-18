
def bolha(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
                desenho(entrada)


    return lista


# desenhar moldura
def desenho(lista_valores):
    tam_coluna= len(entrada) + 2
    tam_linha = max(lista_valores)
    print("." * tam_coluna)
    for i in range(tam_linha,0,-1):
        print('.',end='') # inicio linha
        for j in lista_valores:
            if j >= i:
                print("|", end = '')
            else:
                print(" ", end = '')
        print(".") # fim linha
    print("." * tam_coluna)




entrada = '2 1 3 3 5 4'.split()

for i in range(len(entrada)):
    entrada[i] = int(entrada[i])

desenho(entrada)
#bolha(entrada)









entrada = '1 2 3 4 5'

entrada = entrada.split()
lista = ['1', '2', '3', '4', '5']

lista[0] = int('1')
1


[1, 2, 3, 4, 5]
