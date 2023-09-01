salario_inicial = 1000
ano = 2005
aumento = 1.5
atual = int(input("Informe o ano em que estamos: "))
for i in range(ano + 1, atual + 1):
    salario_inicial += salario_inicial * (aumento / 100)
    aumento = aumento * 2
print("O novo salário desse funcionário é de R${:.2f}".format(salario_inicial))