# -*- coding: utf-8 -*-

ponto_1 = input().split()
ponto_2 = input().split()

x = (float(ponto_2[0]) - float(ponto_1[0])) ** 2
y = (float(ponto_2[1]) - float(ponto_1[1])) ** 2
dist_pontos = (x + y) ** (1 / 2)

print("{:.4f}".format(dist_pontos))
