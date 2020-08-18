
lista_usuarios = []
usuarios = input()
while usuarios != '--':
    lista_usuarios.append(usuarios)
    usuarios = input()


amizades = {}
for i in range(len(lista_usuarios)):
     amizades[lista_usuarios[i]] = []


entrada = input()
while entrada != '--':
    entrada = entrada.split()
    for i in lista_usuarios:
        if i == entrada[0]:
            amizades[i].append(entrada[1])
            amizades[entrada[1]].append(i)
    entrada = input()


print(amizades)
print(lista_usuarios)
"""
lista_usuarios.sort()
for i in range(len(lista_usuarios)):
    for j in range(i+1,len(lista_usuarios)):

        print(lista_usuarios[i], lista_usuarios[j], sep=' ',end=' ')
        print(':', sep=' ',end='')
        interseccao = sorted( (set(amizades[lista_usuarios[i]]) & set(amizades[lista_usuarios[j]])) )
        for k in range(len(interseccao)):
            if k == len(interseccao)-1:
                print('',interseccao[k],end='')
            elif len(interseccao) > 1:
                print('',interseccao[k],sep=' ',end='')

            elif len(interseccao) == 1:
                print('',interseccao[k],end='')
        print()
"""










Gabriel
Beatriz
Guilherme
--

Gabriel Beatriz
Beatriz Guilherme
--

lista_usuarios = ['Gabriel','Beatriz', 'Guilherme']
lista_amigos = ['Gabriel Beatriz', 'Beatriz Guilherme']

{'chave': valor, 'chave': valor, 'chave': valor}

{'Gabriel': [], 'Beatriz': [], 'Guilherme': []}


lista_amigos[0] == 'Gabriel Beatriz'

'Gabriel Beatriz Pedro'.split()
aux = ['Gabriel', 'Beatriz']

if lista_usuarios[0] == aux[0]:
    amizade[lista_usuarios[0]].append(aux[1])
    amizade[aux[1]].append(aux[lista_usuarios[0]])

    amizade['Gabriel'].append('Beatriz')
    amizade['Beatriz'].append('Gabriel'])

{'Gabriel': ['Beatriz'], 'Beatriz': ['Gabriel'], 'Guilherme': []}
















amigos_comum= []
while True:
  entrada = input()
  if entrada == "--":
    break
  amigos_comum = entrada.split() # -> [Beatriz,Guilherme]
  print(amigos_comum)

  for j in amigos:
    if j == amigos_comum[0]:
      amizades[j].append(amigos_comum[1]) # amizades['Gabriel'] = 'Beatriz'
      amizades[amigos_comum[1]].append(j) # amizades['Beatriz'] = 'Gabriel'

print(amizades)
