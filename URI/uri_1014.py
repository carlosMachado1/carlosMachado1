# -*- coding: utf-8 -*-

dist_total = int(input())
gas_usada = float(input())

consumo_medio = dist_total / gas_usada

print("{:.3f} km/l".format(consumo_medio))