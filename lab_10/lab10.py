"""
https://www.ic.unicamp.br/~mc102/labs/roteiro-lab10.html
+-----+
|     |
|  @  |
| @ @ |
|     |
+-----+
2
"""

import copy

# entrada
aux = 0
linha = []
matriz = []
while aux < 2:
    entrada = input()
    if entrada[0] == '+':
        aux = aux + 1

    for i in entrada:
        linha.append(i)

    matriz.append(linha.copy())
    linha.clear()


iteracoes = int(input())

# saida
for i in matriz:
   for j in i:
       print(j,end='')
   print()



aux = 0
cont_vizinhos = 0
mt_aux = copy.deepcopy(matriz)
while aux < iteracoes:
    mt_clone = copy.deepcopy(mt_aux)
    linha = len(mt_aux)
    coluna = len(mt_aux[0])

    for i in range(linha):
        for j in range(coluna):
            if mt_aux[i][j] != '-' and mt_aux[i][j] != '+' and mt_aux[i][j] != '|':
                #print(i,j,mt_aux[i][j])
                #linhas
                if mt_aux[i][j-1] == '@':
                    cont_vizinhos = cont_vizinhos + 1
                if mt_aux[i][j+1] == '@':
                    cont_vizinhos = cont_vizinhos + 1

                #colunas
                if mt_aux[i-1][j] == '@':
                    cont_vizinhos = cont_vizinhos + 1
                if mt_aux[i+1][j] == '@':
                    cont_vizinhos = cont_vizinhos + 1

                #diagonais
                if mt_aux[i-1][j-1] == '@':
                    cont_vizinhos = cont_vizinhos + 1
                if mt_aux[i+1][j+1] == '@':
                    cont_vizinhos = cont_vizinhos + 1
                if mt_aux[i+1][j-1] == '@':
                    cont_vizinhos = cont_vizinhos + 1
                if mt_aux[i-1][j+1] == '@':
                    cont_vizinhos = cont_vizinhos + 1


                if mt_aux[i][j] == '@' and (cont_vizinhos == 2 or cont_vizinhos == 3):#sobrevivencia
                    mt_clone[i][j] = '@'

                if cont_vizinhos >= 4: #morte por superpopulacao
                    mt_clone[i][j] = ' '
                elif cont_vizinhos < 2: #morte por isolamento
                    mt_clone[i][j] = ' '

                if mt_aux[i][j] == ' ' and cont_vizinhos == 3:
                    mt_clone[i][j] = '@'


                cont_vizinhos = 0


    aux = aux + 1
    for i in mt_clone:
       for j in i:
           print(j,end='')
       print()

    mt_aux = copy.deepcopy(mt_clone)


"""
# saida
for i in matriz:
   for j in i:
       print(j,end='')
   print()
"""
