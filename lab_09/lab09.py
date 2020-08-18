
def tupla_float_int(x) :
    x = x[1:-1]
    x = x.split(",")
    f = float(x[0])
    i = int(x[1])
    return (f,i)


soma_lab = 0
soma_pesos = 0
media_prova = 0
nota_labs = input()
nota_provas = input()

nota_labs = [tupla_float_int(x) for x in nota_labs.split()]
prova1, prova2 = [float(x) for x in nota_provas.split()]

for i in nota_labs:
    soma_lab = soma_lab + i[0] * i[1]
    soma_pesos = soma_pesos + i[1]

media_lab = soma_lab/soma_pesos
media_prova = (prova1 * 3 + prova2 * 4)/ 7


print("Media das tarefas de laboratorio:",  format(media_lab, ".1f"))
print("Media das provas:", format(media_prova, ".1f"))

if media_prova >= 5 and media_lab >= 5:
    media_final = 0.7 * media_prova + 0.3 * media_lab
    print("Aprovado(a) por nota e frequencia")
    print("Media final:", format(media_final, ".1f"))
elif media_prova >= 2.5 and media_lab >= 2.5:
    nota_exame = float(input())
    media_preliminar = min(4.9, 0.7 * media_prova + 0.3 * media_lab)
    print("Media preliminar:", format(media_preliminar, ".1f"))
    print("Nota no exame:", format(nota_exame, ".1f"))
    media_final = (media_preliminar + nota_exame)/2

    if media_final >= 5:
        print("Aprovado(a) por nota e frequencia")
        print("Media final:", format(media_final, ".1f"))
    else:
        print("Reprovado(a) por nota")
        print("Media final:", format(media_final, ".1f"))

elif media_prova < 2.5 or media_lab < 2.5:
        media_final = min(media_prova, media_lab)
        print("Reprovado(a) por nota")
        print("Media final:", format(media_final, ".1f"))
