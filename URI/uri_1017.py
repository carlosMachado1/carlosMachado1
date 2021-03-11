# -*- coding: utf-8 -*-

tempo_viagem = int(input())
vel_media = int(input())

dist = tempo_viagem * vel_media

combustivel = dist / 12

print("{:.3f}".format(combustivel))
