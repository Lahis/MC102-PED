# -*- coding: utf-8 -*-

# Script para testar tarefas de laboratÃ³rio de MC102 em ambiente Windows.

# Uso: py executa-testes-windows.py lab<x>.py

# O programa lab<x>.py serÃ¡ testado com todos os arquivos arq<i>.in
# encontrados no diretÃ³rio corrente. Os testes serÃ£o iniciados com i
# igual a 1 e serÃ£o interrompidos quando arq<i>.in nÃ£o for encontrado.

# As saÃ­das serÃ£o comparadas com os arquivos arquivos arq<i>.res.

# Durante o processamento serÃ£o criados e posteriormente removidos
# arquivos arq<i>.out e arq<i>.diff.

import os
import sys

if len(sys.argv) < 2 :
    print("Uso: py executa-testes-windows.py labXX.py")
    sys.exit()

labfile = sys.argv[1]
if not os.path.exists(labfile) :
    print("Arquivo ", labfile, "nÃ£o encontrado.")
    sys.exit()

i = 1
testname = "arq" + str(i).zfill(2)
infile = testname + ".in"

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "\\")

while (os.path.exists(infile)) :
    resfile = testname + ".res"
    if not os.path.exists(resfile) :
      print("Arquivo", resfile, "nÃ£o encontrado.")
      sys.exit()

    outfile = testname + ".out"
    if (os.path.exists(outfile)) :
       answer = input("Arquivo " + outfile + " existente. Pode ser sobrescrito (S/n) ?")
       if answer == "n" or answer == "N" :
         sys.exit()

    difffile = testname + ".diff"
    if (os.path.exists(difffile)) :
       answer = input("Arquivo " + difffile + " existente. Pode ser sobrescrito (S/n) ?")
       if answer == "n" or answer == "N" :
         sys.exit()

    os.system("python " + labfile + " < " + infile + " > " + outfile)
    if os.system("FC " + outfile + " " + resfile + " > " + difffile) == 0 :
       print("Teste ", str(i), ": resultado correto")
    else:
      print("Teste ", str(i), ": resultado incorreto")
      os.system("type " + difffile)
    os.remove(outfile)
    os.remove(difffile)
    i += 1
    testname = "arq" + str(i).zfill(2)
    infile = testname + ".in"
