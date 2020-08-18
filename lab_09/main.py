def tupla_float_int(x):
  x = x[1:-1]
  x = x.split(",")
  f = float(x[0])
  i = int(x[1])
  return (f,i)
notas_laboratorio = [tupla_float_int(x) for x in input().split()]
prova1, prova2 = [float(x) for x in input().split()]

def med_lab(notas_laboratorio):
  peso_labs = 0
  nota_labs = 0
  for notas in notas_laboratorio:
    nota_labs += notas[0] * notas[1]
    peso_labs += notas[1]
  med_lab = nota_labs/peso_labs
  return float(med_lab)
med_provas = ((prova1 * 3) + (prova2 * 4))/7
print(med_provas, med_lab(notas_laboratorio))


if med_lab(notas_laboratorio) >= 5.0 and med_provas >= 5.0:
  media_final2 = 0.7*med_provas + 0.3*med_lab(notas_laboratorio)
  print("Aprovado(a) por nota e frequencia")
  print("Media final:", format(media_final2, '.1f'))

if float(med_lab(notas_laboratorio)) >= 2.5 and med_provas >= 2.5:
  if ((med_lab(notas_laboratorio)) < 5 and med_provas < 5) and (med_lab(notas_laboratorio) >= 2.5 and med_provas >= 2.5):
    print("--------------------------------------------")
    med_preliminar = min(4.9, 0.7*med_provas + 0.3*med_lab(notas_laboratorio))
    exame = float(input())
    print("Media das tarefas de laboratorio:", format(med_lab(notas_laboratorio),'.1f'))
    print("Media das provas:", format(med_provas, '.1f'))
    print("Media preliminar:", format(med_preliminar, '.1f'))
    print("Nota do exame:", exame)
    media_final1 = (med_preliminar + exame)/2
    if media_final1 >= 5.0:
      print("Aprovado(a) por nota e frequencia")
      print("Media final:", format((media_final1), '.1f'))
    else:
      print("Reprovado por nota")
      print("Media final:", format(media_final1, '.1f'))
else:
  media_final3 = min(med_provas, med_lab(notas_laboratorio))
  print("Media das tarefas de laboratorio:", format(med_lab(notas_laboratorio),'.1f'))
  print("Media das provas:", format(med_provas, '.1f'))
  print("Reprovado por nota")
  print("Media final:", format(media_final3, '.1f'))
