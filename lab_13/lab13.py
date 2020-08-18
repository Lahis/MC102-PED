def bolha(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return lista

def moldura_simples(metade, lista):
    salva_pos = -1
    status = False

    global comprimento_original
    global numero_procurado
    global esquerda
    global marco_lista
    comprimento_lista = len(lista)

    if comprimento_lista == comprimento_original:
        for i in range(comprimento_lista):
            print('+-----', end = '')
        print('+')

        for i in range(comprimento_lista):
            print('| ' + format(lista[i],"03d") + ' ', end = '')
        print('|')

        for i in range(comprimento_lista):
            print('+-----', end = '')
        print('+')





def moldura_lista(metade, lista):
    salva_pos = -1
    status = False

    global comprimento_original
    global numero_procurado
    global esquerda
    global marco_lista
    comprimento_lista = len(lista)

    if comprimento_lista == comprimento_original:
        for i in range(comprimento_lista):
            if i == metade:
                print('+=====', end = '')
            else:
                print('+-----', end = '')
        print('+')

        for i in range(comprimento_lista):
            if i == metade:
                print('||' + format(lista[i],"03d") + '|', end = '')
                if lista[i] == numero_procurado:
                    salva_pos = i
                    status = True
            else:
                print('| ' + format(lista[i],"03d") + ' ', end = '')
        print('|')

        for i in range(comprimento_lista):
            if i == metade:
                print('+=====', end = '')
            else:
                print('+-----', end = '')
        print('+')

    elif comprimento_lista != comprimento_original:
        for i in range(marco_lista):
            print(' '*6, end = '')
        print('',end='')

        for i in range(comprimento_lista):
            if i == metade:
                print('+=====', end = '')
            else:
                print('+-----', end = '')
        print('+')

        for i in range(marco_lista):
            print(' '*6, end = '')
        print('',end='')

        for i in range(comprimento_lista):
            if i == metade:
                print('||' + format(lista[i],"03d") + '|', end = '')
                if lista[i] == numero_procurado:
                    salva_pos = marco_lista + i
                    status = True
            else:
                print('| ' + format(lista[i],"03d") + ' ', end = '')
        print('|')

        for i in range(marco_lista):
            print(' '*6, end = '')
        print('',end='')

        for i in range(comprimento_lista):
            if i == metade:
                print('+=====', end = '')
            else:
                print('+-----', end = '')
        print('+')

    if comprimento_lista == 1 and lista[0] != numero_procurado:
        print('O elemento nao foi encontrado')
        exit()

    return status, salva_pos



numero_procurado = int(input())
entrada = input().split()
#numero_procurado = 3
#entrada = '2 3 4 8 11 15 17'.split()
print('Elemento procurado: ' + format(numero_procurado,"03d"))


for i in range(len(entrada)):
    entrada[i] = int(entrada[i])

comprimento_original = len(entrada)
moldura_simples(numero_procurado, entrada)

#verifica se esta ordenada
lista_ordenada = entrada.copy()
lista_ordenada = bolha(lista_ordenada)
for i in range(len(entrada)):
    if lista_ordenada[i] != entrada[i]:
        print("Lista nao ordenada")
        exit()

# calculo metade
if (len(entrada) % 2) == 0:
    metade = (len(entrada) // 2) -1
else:
    metade = (len(entrada) // 2)

cont = 0
index = 0
list_aux = []
esquerda = False
marco_lista = 0
isFound, index = moldura_lista(metade,entrada)
while isFound != True:

    if numero_procurado > entrada[metade]:
        list_aux = entrada[metade + 1:]
        esquerda = False
        marco_lista = marco_lista + metade +1
    elif numero_procurado < entrada[metade]:
        list_aux = entrada[:metade]
        esquerda = True
        marco_lista = marco_lista


    # calculo metade
    if (len(list_aux) % 2) == 0:
        metade = (len(list_aux) // 2) -1
    else:
        metade = (len(list_aux) // 2)

    cont +=1
    entrada = list_aux
    isFound, index = moldura_lista(metade,entrada)

print('Encontrado na posicao:',index)
