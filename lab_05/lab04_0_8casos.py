m_corporal = float(input())
idade 	   = int(input())

apto = 0
impedimento = 0

print("Massa corporal:", m_corporal)
print("Idade:", idade)

if idade < 16:
    sintomas_14_dias = str(input())
    viagem_30_dias = str(input())
    contato_covid_30_dias = str(input())
    primeira_doacao = str(input())
    print("Febre ou sintomas gripais:", sintomas_14_dias )
    print("Viagem recente ao exterior:", viagem_30_dias )
    print("Contato com caso de COVID-19:", contato_covid_30_dias )
    print("Primeira doacao:", primeira_doacao)

    if primeira_doacao == "S":
        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)
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
            if doacoes_12_meses <= 3:
                if doacoes_12_meses > 0:
                    if meses_ultima_doacao <= 2:
                        impedimento = 1
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            elif doacoes_12_meses > 3:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")
            if gravida_ou_amamentando == "S":
                impedimento = 1
                print("Impedimento: gravida ou amamentando")
        elif sexo == "M":
            if doacoes_12_meses <= 4:
                if doacoes_12_meses > 0:
                    if meses_ultima_doacao >= 3:
                        print("Agende um horario para triagem completa")
                    else:
                        impedimento = 1
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            else:
                    impedimento = 1
                    print("Impedimento: numero maximo de doacoes anuais foi atingido")
    if m_corporal < 50:
        print("Impedimento: abaixo da massa corporal minima")
    print("Impedimento: menor de 16 anos")
if idade >= 16 and idade < 60:
    if idade < 18:
        documento = str(input())
        sintomas_14_dias = str(input())
        viagem_30_dias = str(input())
        contato_covid_30_dias = str(input())
        primeira_doacao = str(input())
        print("Documento de autorizacao:", documento)
        print("Febre ou sintomas gripais:", sintomas_14_dias )
        print("Viagem recente ao exterior:", viagem_30_dias )
        print("Contato com caso de COVID-19:", contato_covid_30_dias )
        print("Primeira doacao:", primeira_doacao)

        if documento == "S":
            if primeira_doacao == "S":
                sexo = str(input())
                print("Sexo biologico:", sexo)
                if sexo == "F":
                    gravida_ou_amamentando = str(input())
                    print("Gravida ou amamentando:", gravida_ou_amamentando)
                    if gravida_ou_amamentando == "N":
                        print("Agende um horario para triagem completa")
                    elif gravida_ou_amamentando == "S":
                        impedimento = 1
                        print("Impedimento: gravida ou amamentando")
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
                    if doacoes_12_meses == 0:
                        if gravida_ou_amamentando == "N":
                            print("Agende um horario para triagem completa")
                    if doacoes_12_meses <= 3:
                        if doacoes_12_meses > 0:
                            if meses_ultima_doacao >= 2:
                                if gravida_ou_amamentando == "N":
                                    print("Agende um horario para triagem completa")
                            else:
                                impedimento = 1
                                print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                    elif doacoes_12_meses > 3:
                        impedimento = 1
                        print("Impedimento: numero maximo de doacoes anuais foi atingido")
                    if gravida_ou_amamentando == "S":
                        impedimento = 1
                        print("Impedimento: gravida ou amamentando")
                elif sexo == "M":
                    if doacoes_12_meses <= 4:
                        if doacoes_12_meses > 0:
                            if meses_ultima_doacao >= 3:
                                print("Agende um horario para triagem completa")
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
                    if gravida_ou_amamentando == "N":
                        print("Agende um horario para triagem completa")
                    elif gravida_ou_amamentando == "S":
                        impedimento = 1
                        print("Impedimento: gravida ou amamentando")
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
                    if doacoes_12_meses == 0:
                        if gravida_ou_amamentando == "N":
                            print("Agende um horario para triagem completa")
                    if doacoes_12_meses <= 3:
                        if doacoes_12_meses > 0:
                            if meses_ultima_doacao >= 2:
                                if gravida_ou_amamentando == "N":
                                    print("Agende um horario para triagem completa")
                            else:
                                impedimento = 1
                                print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                    elif doacoes_12_meses > 3:
                        impedimento = 1
                        print("Impedimento: numero maximo de doacoes anuais foi atingido")
                    if gravida_ou_amamentando == "S":
                        impedimento = 1
                        print("Impedimento: gravida ou amamentando")
                elif sexo == "M":
                    if doacoes_12_meses <= 4:
                        if doacoes_12_meses > 0:
                            if meses_ultima_doacao >= 3:
                                print("Agende um horario para triagem completa")
                            else:
                                impedimento = 1
                                print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                    else:
                        impedimento = 1
                        print("Impedimento: numero maximo de doacoes anuais foi atingido")
            impedimento = 1
            print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
    else:
        sintomas_14_dias = str(input())
        viagem_30_dias = str(input())
        contato_covid_30_dias = str(input())
        primeira_doacao = str(input())
        print("Febre ou sintomas gripais:", sintomas_14_dias )
        print("Viagem recente ao exterior:", viagem_30_dias )
        print("Contato com caso de COVID-19:", contato_covid_30_dias )
        print("Primeira doacao:", primeira_doacao)

        if primeira_doacao == "S":
            sexo = str(input())
            print("Sexo biologico:", sexo)
            if sexo == "M":
                print("Agende um horario para triagem completa")
            if sexo == "F":
                gravida_ou_amamentando = str(input())
                print("Gravida ou amamentando:", gravida_ou_amamentando)
                if gravida_ou_amamentando == "N":
                    apto = 1
                elif gravida_ou_amamentando == "S":
                    impedimento = 1
                    print("Impedimento: gravida ou amamentando")
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
                if doacoes_12_meses == 0:
                    if gravida_ou_amamentando == "N":
                        print("Agende um horario para triagem completa")
                if doacoes_12_meses <= 3:
                    if doacoes_12_meses > 0:
                        if meses_ultima_doacao >= 2:
                            if gravida_ou_amamentando == "N":
                                print("Agende um horario para triagem completa")
                        else:
                            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
                elif doacoes_12_meses > 3:
                    print("Impedimento: numero maximo de doacoes anuais foi atingido")
                if gravida_ou_amamentando == "S":
                    print("Impedimento: gravida ou amamentando")
            elif sexo == "M":
                if doacoes_12_meses >= 4:
                    impedimento = 1
                    print("Impedimento: numero maximo de doacoes anuais foi atingido")

                if doacoes_12_meses > 0:
                    if meses_ultima_doacao < 2:
                        impedimento = 1
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
if idade >= 60 and idade < 69:
    sintomas_14_dias = str(input())
    viagem_30_dias = str(input())
    contato_covid_30_dias = str(input())
    primeira_doacao = str(input())

    print("Febre ou sintomas gripais:", sintomas_14_dias )
    print("Viagem recente ao exterior:", viagem_30_dias )
    print("Contato com caso de COVID-19:", contato_covid_30_dias )
    print("Primeira doacao:", primeira_doacao)

    if primeira_doacao == "S":
        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)
            if gravida_ou_amamentando == "N":
                print("Agende um horario para triagem completa")
            elif gravida_ou_amamentando == "S":
                print("Impedimento: gravida ou amamentando")
        print("Impedimento: maior de 60 anos e primeira doacao")
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
            if doacoes_12_meses == 0:
                if gravida_ou_amamentando == "N":
                    print("Agende um horario para triagem completa")
            if doacoes_12_meses <= 3:
                if doacoes_12_meses > 0:
                    if meses_ultima_doacao >= 2:
                        if gravida_ou_amamentando == "N":
                            print("Agende um horario para triagem completa")
                    else:
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            elif doacoes_12_meses > 3:
                print("Impedimento: numero maximo de doacoes anuais foi atingido")
            if gravida_ou_amamentando == "S":
                print("Impedimento: gravida ou amamentando")
        elif sexo == "M":
            if doacoes_12_meses <= 4:
                if doacoes_12_meses > 0:
                    if meses_ultima_doacao >= 3:
                        print("Agende um horario para triagem completa")
                    else:
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            else:
                print("Impedimento: numero maximo de doacoes anuais foi atingido")

elif idade >= 69:
    sintomas_14_dias = str(input())
    viagem_30_dias = str(input())
    contato_covid_30_dias = str(input())
    primeira_doacao = str(input())
    print("Febre ou sintomas gripais:", sintomas_14_dias )
    print("Viagem recente ao exterior:", viagem_30_dias )
    print("Contato com caso de COVID-19:", contato_covid_30_dias )
    print("Primeira doacao:", primeira_doacao)
    if primeira_doacao == "S":
        sexo = str(input())
        print("Sexo biologico:", sexo)
        if sexo == "F":
            gravida_ou_amamentando = str(input())
            print("Gravida ou amamentando:", gravida_ou_amamentando)
            if gravida_ou_amamentando == "N":
                print("Agende um horario para triagem completa")
            elif gravida_ou_amamentando == "S":
                impedimento = 1
                print("Impedimento: gravida ou amamentando")
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
            if doacoes_12_meses == 0:
                if gravida_ou_amamentando == "N":
                    print("Agende um horario para triagem completa")
            if doacoes_12_meses <= 3:
                if doacoes_12_meses > 0:
                    if meses_ultima_doacao >= 2:
                        if gravida_ou_amamentando == "N":
                            print("Agende um horario para triagem completa")
                    else:
                        impedimento = 1
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            elif doacoes_12_meses > 3:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")
            if gravida_ou_amamentando == "S":
                impedimento = 1
                print("Impedimento: gravida ou amamentando")
        elif sexo == "M":
            if doacoes_12_meses <= 4:
                if doacoes_12_meses > 0:
                    if meses_ultima_doacao >= 3:
                        print("Agende um horario para triagem completa")
                    else:
                        impedimento = 1
                        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
            else:
                impedimento = 1
                print("Impedimento: numero maximo de doacoes anuais foi atingido")
    impedimento = 1
    print("Impedimento: maior de 69 anos")


if sintomas_14_dias == "S":
    impedimento = 1
    print("Impedimento: febre ou sintomas gripais")

if viagem_30_dias == "S":
    impedimento = 1
    print("Impedimento: viagem recente ao exterior")

if contato_covid_30_dias == "S":
    impedimento = 1
    print("Impedimento: contato com caso de COVID-19")


if apto == 1 and impedimento == 0:
    print("Agende um horario para triagem completa")
