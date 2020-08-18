from math import floor

valor = float(input())
dias_atraso = int(input())
multa = valor * 0.02
juros = valor * (0.033/100) * dias_atraso
valor_total = valor + multa + juros
pag_min = valor_total * 0.1 # incoerencia com exemplo

print("Valor: R$",  format(valor,".2f"))
print("Multa: R$", format(multa,".2f"))
print("Juros: R$", format(juros,".2f"))
print("Valor total: R$", format(valor_total,".2f") )
#print("Valor minimo para renegociacao: R$", pag_min)
#print("Valor minimo para renegociacao: R$", format(floor(pag_min),".2f"))
print("Valor minimo para renegociacao: R$", format((pag_min),".2f"))
