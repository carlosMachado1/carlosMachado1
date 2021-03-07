# -*- coding: utf-8 -*-


valores = input().split()
valor_1 = int(valores[0])
valor_2 = int(valores[1])
valor_3 = int(valores[2])

maior = int((valor_1 + valor_2 + abs(valor_1 - valor_2)) / 2)

if maior > valor_3:
    print("{} eh o maior".format(maior))
else:
    maior = valor_3
    print("{} eh o maior".format(maior))
