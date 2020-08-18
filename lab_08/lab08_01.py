lista = input().split()
palavras = []
numeros = []
hashtags = []
emoticons = []

for x in lista:
    if x.isalpha():
        palavras.append(x)
    elif x.lstrip('-').isdigit():
        numeros.append(x)
    elif x[0] == "#" and x[1:].isalpha():
        hashtags.append(x)
    else:
        emoticons.append(x)

# Imprime todas as palavras
print("Palavra(s):", end="")
for i in range(len(palavras)):
    print("",palavras[i], end="")
print()

# Imprime todos os numeros
print("Numero(s):", end="")
for i in range(len(numeros)):
    print("",numeros[i], end="")
print()

# Imprime todas as hashtags
print("Hashtag(s):", end="")
for i in range(len(hashtags)):
    print("",hashtags[i], end="")
print()

# Imprime os emoticons
print("Emoticon(s):", end="")
for i in range(len(emoticons)):
    print("",emoticons[i], end="")
