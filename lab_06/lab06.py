percurso = 33

qtd_nivel_0 = 0
qtd_nivel_1 = 0
qtd_nivel_2 = 0

tempo = 0
tempo_medio = 0.
max_velocidade = 0.
min_velocidade = 1000

soma_tempo = 0
cont = 0

tempo = float(input())
while tempo != -1:
    if tempo < 180:
        qtd_nivel_0 +=1
    elif tempo >= 180 and tempo < 240:
        qtd_nivel_1 +=1
    elif tempo >= 240:
        qtd_nivel_2 +=1

    tempo_min = tempo/60
    velocidade = percurso/tempo_min

    if velocidade > max_velocidade:
        max_velocidade = velocidade

    if velocidade < min_velocidade:
        min_velocidade = velocidade

    soma_tempo += tempo

    cont += 1

    tempo = int(input())

tempo_medio = soma_tempo/cont

print("Caracois no nivel 0:", qtd_nivel_0)
print("Caracois no nivel 1:", qtd_nivel_1)
print("Caracois no nivel 2:", qtd_nivel_2)
print("Tempo medio:", round(tempo_medio,1), "s")
print("Velocidade maxima:", round(max_velocidade,1), "cm/min")
print("Velocidade minima:", round(min_velocidade,1), "cm/min")
