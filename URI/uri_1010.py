# -*- coding: utf-8 -*-

peca_1 = input().split()
peca_2 = input().split()

val_pago_1 = int(peca_1[1]) * float(peca_1[2])
val_pago_2 = int(peca_2[1]) * float(peca_2[2])

val_total = val_pago_1 + val_pago_2

print("VALOR A PAGAR: R$ {:.2f}".format(val_total))
