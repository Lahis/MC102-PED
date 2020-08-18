lado_1 = float(input())
lado_2 = float(input())
lado_3 = float(input())

if (lado_1 > lado_2) and (lado_1 > lado_3):
    A = lado_1
    B = lado_2
    C = lado_3
elif (lado_2 > lado_1) and (lado_2 > lado_3):
    A = lado_2
    B = lado_1
    C = lado_3
elif (lado_3 > lado_1) and (lado_3 > lado_2):
    A = lado_3
    B = lado_1
    C = lado_2
else:
    A = lado_1
    B = lado_2
    C = lado_3


if int(A) <= 0 and int(B) <= 0 and int(C) <= 0:
    print("Valores invalidos na entrada")
if (A >= B + C) or (B >= A + C) or (C >= B + A):
    print("Valores invalidos na entrada")
else:
    if A == B == C:
        print("Triangulo equilatero")
    elif A == B or A == C or B == C:
        print("Triangulo isosceles")
    elif A != B != C:
        print("Triangulo escaleno")

    if A*A < (B*B + C*C):
        print("Triangulo acutangulo")
    elif A*A > (B*B + C*C):
        print("Triangulo obtusangulo")
    elif A*A == (B*B + C*C):
        print("Triangulo retangulo")
