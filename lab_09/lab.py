def tupla_float_int(x) :
    x = x[1:-1]       # remove parenteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla

t= [tupla_float_int(x) for x in input().split()]
provas = [float(x) for x in input().split()]

soma1=0
for i in range(len(t)):
	soma1 = soma1 +(t[i][0] * t[i][1])
	lista=list()
	lista.append(soma1)
media1=sum(lista)
#print(media1)
soma=0
for j in range(len(t)):
	soma =soma +  t[j][1]
	#print(soma)
	peso=list()
	peso.append(soma)
#	print(sum(len(peso),end" "))
media=sum(peso)
#print(media)

mediaLab= media1 / media
print ("Media das tarefas de laboratorio:",format(mediaLab,'.1f'))

media_provas = (provas[0]*3 + provas[1]*4) / 7
print ("Media das provas:",format(media_provas,'.1f'))

Mpreliminar = (0.7 * media_provas  + 0.3 * mediaLab)


if media_provas >= 5 and mediaLab >= 5:
	Mpreliminar = (0.7 * media_provas  + 0.3 * mediaLab
	MFinal = max(5, Mpreliminar)
	MFinal = min(10, MFinal)
	print ("Aprovado(a) por nota e frequencia")
	print ("Media final:",format(MFinal,'.1f'))

elif media_provas >= 2.5 and mediaLab >= 2.5:
	Exame = float(input())
	print("media preliminar:",format(Mpreliminar,'.1f'))
	print ("Nota no exame:",format(Exame,'.1f'))

	MFinal = (min(media_provas, mediaLab) + Exame)/2
	if MFinal >= 5:
		print ("Aprovado(a) por nota e frequencia")
	else:
		print ("Reprovado(a) por nota")
	print ("Media final:",format(MFinal,'.1f'))

else:
		print ("Reprovado(a) por nota")
		MFinal = min(media_provas, mediaLab)
		print ("Media final:",format(MFinal,'.1f'))
