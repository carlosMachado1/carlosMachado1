# -*- coding: utf-8 -*-

vel_rel = (90 - 60)
dist_final = int(input())

tempo = int((dist_final / vel_rel) * 60)

print("{} minutos".format(tempo))
