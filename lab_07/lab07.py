def quadrado_polig(dimensao,caractere):
    for i in range(dimensao):
        print(dimensao * caractere)

def triangulo_polig(dimensao,caractere):
    tab = dimensao
    for coluna in range(1, dimensao*2, 2):
        for espace in range(tab-1):
            print(" ",end = '')
        for linha in range(coluna):
            print(caractere, end = '')
        print("")
        tab = tab -1

def losangulo_polig(dimensao,caractere):
    tab = dimensao
    for coluna in range(1, dimensao*2, 2):
        for espace in range(tab-1):
            print(" ",end = '')
        for linha in range(coluna):
            print(caractere, end = '')
        print("")
        tab = tab - 1

    tab = 1 #9,1,-2: 9
    for coluna in range(dimensao*2-2, 1, -2):
        for espace in range(tab):
            print(" ",end = '')
        for linha in range(coluna-1):
            print(caractere, end = '')
        print("")
        tab = tab + 1

def hex_polig(dimensao,caractere):
    tab = dimensao
    for coluna in range(dimensao, dimensao*3-1, 2):
        for espace in range(tab-1):
            print(" ",end = '')
        for linha in range(coluna):
            print(caractere, end = '')
        print("")
        tab = tab - 1

#3,5,7,5,3    4,6,8,10,8,6,4     5,7,9,11,13,11,9,7,5
    tab = 1
    for coluna in range(3*dimensao-4, dimensao-1, -2):
        for espace in range(tab):
            print(" ",end = '')
        for linha in range(coluna):
            print(caractere, end = '')
        print("")
        tab = tab + 1


def oct_polig(dimensao,caractere):
    tab = dimensao
    for coluna in range(dimensao, dimensao*3-1, 2):
        for espace in range(tab-1):
            print(" ",end = '')
        for linha in range(coluna):
            print(caractere, end = '')
        print("")
        tab = tab - 1

    for lado in range(dimensao-1):
        print(caractere*(dimensao*3-2))

#3,5,7,7,7,5,3    4,6,8,8,8,8,6,4     5,7,9,11,13,13,13,13,13,11,9,7,5
    tab = 1
    for coluna in range(3*dimensao-4, dimensao-1, -2):
        for espace in range(tab):
            print(" ",end = '')
        for linha in range(coluna):
            print(caractere, end = '')
        print("")
        tab = tab + 1



poligono = str(input())
caractere = str(input())
dimensao = int(input())

quadrado  = 'Q'
triangulo = 'T'
losango   = 'L'
hexagono  = 'H'
octogono  = 'O'

identificadores = [quadrado, triangulo, losango, hexagono, octogono]

isValid = False
for i in identificadores:
    if i == poligono:
        isValid = True
        break

if isValid == False:
    print('Identificador invalido.')
else:
    if dimensao < 3:
        print('Dimensao invalida.')
        isValid = False

if isValid == True:
    if poligono == quadrado:
        quadrado_polig(dimensao,caractere)
    if poligono == triangulo:
        triangulo_polig(dimensao,caractere)
    if poligono == losango:
        losangulo_polig(dimensao,caractere)
    if poligono == hexagono:
        hex_polig(dimensao,caractere)
    if poligono == octogono:
        oct_polig(dimensao,caractere)
