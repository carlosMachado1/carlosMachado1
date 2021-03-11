# -*- coding: utf-8 -*-

valor = int(input())

mensagem = "{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n" +\
    "{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n" +\
    "{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00"

cem = valor // 100
cinquenta = (valor % 100) // 50
vinte = ((valor % 100) % 50) // 20
dez = (((valor % 100) % 50) % 20) // 10
cinco = ((((valor % 100) % 50) % 20) % 10) // 5
dois = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
um = ((((((valor % 100) % 50) % 20) % 10) % 5) % 2) // 1


print(mensagem.format(valor, cem, cinquenta, vinte, dez, cinco, dois, um))
