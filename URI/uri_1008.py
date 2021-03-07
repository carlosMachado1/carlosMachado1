id_funcionario = int(input())
horas_trabalhadas = int(input())
sal_hora = float(input())

sal_mensal = horas_trabalhadas * sal_hora

print("NUMBER = {}".format(id_funcionario))
print("SALARY = U$ {:.2f}".format(sal_mensal))
