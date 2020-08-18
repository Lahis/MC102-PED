
def questoes_gerais ():
    global sintomas_14_dias, viagem_30_dias, contato_covid_30_dias, primeira_doacao
    sintomas_14_dias = str(input())
    viagem_30_dias = str(input())
    contato_covid_30_dias = str(input())
    primeira_doacao = str(input())
    print("Febre ou sintomas gripais:", sintomas_14_dias )
    print("Viagem recente ao exterior:", viagem_30_dias )
    print("Contato com caso de COVID-19:", contato_covid_30_dias )
    print("Primeira doacao:", primeira_doacao)

def massa_corporal():
    global impedimento, apto
    if m_corporal < 50:
        impedimento = 1
        print("Impedimento: abaixo da massa corporal minima")
    else:
        apto = 1

def sintomas():
    global impedimento, apto
    if sintomas_14_dias == "S":
        impedimento = 1
        print("Impedimento: febre ou sintomas gripais")
    else:
        apto = 1

    if viagem_30_dias == "S":
        impedimento = 1
        print("Impedimento: viagem recente ao exterior")
    else:
        apto = 1

    if contato_covid_30_dias == "S":
        impedimento = 1
        print("Impedimento: contato com caso de COVID-19")
    else:
        apto = 1

def gravida_amamentando():
    global impedimento, apto
    if sexo == "F":
        if gravida_ou_amamentando == "N":
            apto = 1
        elif gravida_ou_amamentando == "S":
            impedimento = 1
            print("Impedimento: gravida ou amamentando")

apto = 0
impedimento = 0

m_corporal = float(input())
idade 	   = int(input())
sintomas_14_dias = ""
viagem_30_dias = ""
contato_covid_30_dias = ""
primeira_doacao = ""
sexo = ""
gravida_ou_amamentando = ""


print("Massa corporal:", m_corporal)
print("Idade:", idade)

if idade < 16:
    questoes_gerais ()

    if primeira_doacao == "S":
        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)

        massa_corporal()
        impedimento = 1
        print("Impedimento: menor de 16 anos")
        sintomas()

    elif primeira_doacao == "N":
        doacoes_12_meses = int(input())
        print("Doacoes nos ultimos 12 meses:", doacoes_12_meses)
        if doacoes_12_meses > 0:
            meses_ultima_doacao = int(input())
            print("Meses desde ultima doacao:")

        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)

            massa_corporal()
            impedimento = 1
            print("Impedimento: menor de 16 anos")

            if doacoes_12_meses < 3:
                apto = 1
            elif doacoes_12_meses > 3:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")

            if doacoes_12_meses > 0:
                if meses_ultima_doacao <= 2:
                    impedimento = 1
                    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                else:
                    apto = 1

        elif sexo == "M":
            massa_corporal()
            impedimento = 1
            print("Impedimento: menor de 16 anos")

            if doacoes_12_meses < 4:
                apto = 1
            else:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")

            if doacoes_12_meses > 0:
                if meses_ultima_doacao > 3:
                    apto = 1
                else:
                    impedimento = 1
                    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
if idade >= 16 and idade < 60:
    if idade < 18:
        documento = str(input())
        print("Documento de autorizacao:", documento)
        questoes_gerais ()

        if documento == "S":
            if primeira_doacao == "S":
                sexo = str(input())
                print("Sexo biologico:", sexo)
                if sexo == "F":
                    gravida_ou_amamentando = str(input())
                    print("Gravida ou amamentando:", gravida_ou_amamentando)

                massa_corporal()
                sintomas()
            elif primeira_doacao == "N":
                doacoes_12_meses = int(input())
                print("Doacoes nos ultimos 12 meses:", doacoes_12_meses)
                if doacoes_12_meses > 0:
                    meses_ultima_doacao = int(input())
                    print("Meses desde ultima doacao:")

                sexo = str(input())
                print("Sexo biologico:", sexo)
                if sexo == "F":
                    gravida_ou_amamentando = str(input())
                    print("Gravida ou amamentando:", gravida_ou_amamentando)

                    massa_corporal()
                    sintomas()

                    if doacoes_12_meses < 3:
                        apto = 1
                    elif doacoes_12_meses > 3:
                        impedimento = 1
                        print("Impedimento: numero maximo de doacoes anuais foi atingido")

                    if doacoes_12_meses > 0:
                        if meses_ultima_doacao <= 2:
                            impedimento = 1
                            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                        else:
                            apto = 1
                elif sexo == "M":
                    massa_corporal()
                    sintomas()

                    if doacoes_12_meses < 4:
                        if doacoes_12_meses > 0:
                            if meses_ultima_doacao > 3:
                                apto = 1
                            else:
                                impedimento = 1
                                print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                    else:
                        impedimento = 1
                        print("Impedimento: numero maximo de doacoes anuais foi atingido")
        else:
            if primeira_doacao == "S":
                sexo = str(input())
                print("Sexo biologico:", sexo)
                if sexo == "F":
                    gravida_ou_amamentando = str(input())
                    print("Gravida ou amamentando:", gravida_ou_amamentando)

                massa_corporal()
                impedimento = 1
                print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
                sintomas()
            elif primeira_doacao == "N":
                doacoes_12_meses = int(input())
                print("Doacoes nos ultimos 12 meses:", doacoes_12_meses)
                if doacoes_12_meses > 0:
                    meses_ultima_doacao = int(input())
                    print("Meses desde ultima doacao:")

                sexo = str(input())
                print("Sexo biologico:", sexo)
                if sexo == "F":
                    gravida_ou_amamentando = str(input())
                    print("Gravida ou amamentando:", gravida_ou_amamentando)

                    massa_corporal()
                    impedimento = 1
                    print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
                    sintomas()

                    if doacoes_12_meses < 3:
                        apto = 1
                    elif doacoes_12_meses > 3:
                        impedimento = 1
                        print("Impedimento: numero maximo de doacoes anuais foi atingido")

                    if doacoes_12_meses > 0:
                        if meses_ultima_doacao >= 2:
                            apto = 1
                        else:
                            impedimento = 1
                            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                elif sexo == "M":
                    massa_corporal()
                    impedimento = 1
                    print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
                    sintomas()

                    if doacoes_12_meses < 4:
                        apto = 1
                    else:
                        impedimento = 1
                        print("Impedimento: numero maximo de doacoes anuais foi atingido")

                    if doacoes_12_meses > 0:
                        if meses_ultima_doacao > 3:
                            apto = 1
                        else:
                            impedimento = 1
                            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
    else:
        questoes_gerais ()

        if primeira_doacao == "S":
            sexo = str(input())
            print("Sexo biologico:", sexo)
            if sexo == "M":
                if m_corporal < 50:
                    impedimento = 1
                    print("Impedimento: abaixo da massa corporal minima")
                else:
                    apto = 1

                sintomas()
            if sexo == "F":
                gravida_ou_amamentando = str(input())
                print("Gravida ou amamentando:", gravida_ou_amamentando)
                if m_corporal < 50:
                    impedimento = 1
                    print("Impedimento: abaixo da massa corporal minima")
                else:
                    apto = 1
                sintomas()
        elif primeira_doacao == "N":
            doacoes_12_meses = int(input())
            print("Doacoes nos ultimos 12 meses:", doacoes_12_meses)
            if doacoes_12_meses > 0:
                meses_ultima_doacao = int(input())
                print("Meses desde ultima doacao:", meses_ultima_doacao)

            sexo = str(input())
            print("Sexo biologico:", sexo)
            if sexo == "F":
                gravida_ou_amamentando = str(input())
                print("Gravida ou amamentando:", gravida_ou_amamentando)

                massa_corporal()
                sintomas()

                if doacoes_12_meses < 3:
                    apto = 1
                elif doacoes_12_meses > 3:
                    impedimento = 1
                    print("Impedimento: numero maximo de doacoes anuais foi atingido")

                if doacoes_12_meses > 0:
                    if meses_ultima_doacao >= 2:
                        apto = 1
                    else:
                        impedimento = 1
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            elif sexo == "M":
                massa_corporal()
                sintomas()

                if doacoes_12_meses < 4:
                    apto = 1
                else:
                    impedimento = 1
                    print("Impedimento: numero maximo de doacoes anuais foi atingido")

                if doacoes_12_meses > 0:
                    if meses_ultima_doacao > 3:
                        apto = 1
                    else:
                        impedimento = 1
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
if idade >= 60 and idade < 69:
    questoes_gerais ()
    if primeira_doacao == "S":
        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)
        massa_corporal()
        impedimento = 1
        print("Impedimento: maior de 60 anos e primeira doacao")
        sintomas()
    elif primeira_doacao == "N":
        doacoes_12_meses = int(input())
        print("Doacoes nos ultimos 12 meses:", doacoes_12_meses)
        if doacoes_12_meses > 0:
            meses_ultima_doacao = int(input())
            print("Meses desde ultima doacao:")

        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)
            massa_corporal()
            sintomas()
            if doacoes_12_meses < 3:
                apto = 1
            elif doacoes_12_meses > 3:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")

            if doacoes_12_meses > 0:
                if meses_ultima_doacao >= 2:
                        apto = 1
                else:
                    impedimento = 1
                    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")

        elif sexo == "M":
            massa_corporal()
            sintomas()

            if doacoes_12_meses < 4:
                apto = 1
            else:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")

            if doacoes_12_meses > 0:
                if meses_ultima_doacao > 3:
                    apto = 1
                else:
                    impedimento = 1
                    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
elif idade >= 69:
    questoes_gerais ()
    if primeira_doacao == "S":
        sexo = str(input())
        print("Sexo biologico:", sexo)
        if  sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)
        massa_corporal()
        impedimento = 1
        print("Impedimento: maior de 69 anos")
        sintomas()

    elif primeira_doacao == "N":
        doacoes_12_meses = int(input())
        print("Doacoes nos ultimos 12 meses:", doacoes_12_meses)
        if doacoes_12_meses > 0:
            meses_ultima_doacao = int(input())
            print("Meses desde ultima doacao:")

        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)

            massa_corporal()
            impedimento = 1
            print("Impedimento: maior de 69 anos")
            sintomas()

            if doacoes_12_meses < 3:
                apto = 1
            elif doacoes_12_meses > 3:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")

            if doacoes_12_meses > 0:
                if meses_ultima_doacao >= 2:
                    apto = 1
                else:
                    impedimento = 1
                    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
        elif sexo == "M":
            massa_corporal()
            impedimento = 1
            print("Impedimento: maior de 69 anos")
            sintomas()

            if doacoes_12_meses < 4:
                apto = 1
            else:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")

            if doacoes_12_meses > 0:
                if meses_ultima_doacao > 3:
                    apto = 1
                else:
                    impedimento = 1
                    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")


gravida_amamentando()

if apto == 1 and impedimento == 0:
    print("Agende um horario para triagem completa")
