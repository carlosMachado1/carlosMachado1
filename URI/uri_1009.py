nome = input()
sal_fixo = float(input())
val_vendas = float(input())
comissao = 15 / 100

sal = sal_fixo + (val_vendas * comissao)

print("TOTAL = R$ {:.2f}".format(sal))
