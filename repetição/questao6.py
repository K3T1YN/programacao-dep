horas = int(input("Quantidade de horas trabalhadas no mês: "))
turno = str(input("Turno de trabalho do funcionário: [M - matutino, V - vespertino, N - noturno]"))
categoria = str(input("Categoria do funcionário: [O - operário; G - gerente]"))
salario_minimo = 450
if categoria == 'G' and turno == 'N':
    valor1 = (salario_minimo * 18) / 100
    salario_inicial = horas * valor1
    if salario_inicial <= 300:
        alimentação1 = (salario_inicial * 20) / 100
    print("Valor da hora trabalhada para a categoria G e turno N: R${}".format(valor1))
    print("O salário inicial desse funcionário é de R${}".format(salario_inicial))
    print("O valor do seu auxílio alimentação será de R${}".format(alimentação1))
if categoria == 'G' and turno == 'M' or categoria == 'G' and turno == 'V':
    valor2 = (salario_minimo * 15) / 100
    salario_inicial2 = horas * valor2
    print("Valor da hora trabalhada para a categoria G e turno M/V: R${}".format(valor2))
    print("O salário inicial desse funcionário é de R${}".format(salario_inicial2))
if categoria == 'O' and turno == 'N':
    valor3 = (salario_minimo * 13) / 100
    salario_inicial3 = horas * valor3
    print("Valor da hora trabalhada para a categoria O e turno N: R${}".format(valor3))
    print("O salário inicial desse funcionário é de R${}".format(salario_inicial3))
if categoria == 'O' and turno == 'M' or categoria == 'O' and turno == 'V':
    valor4 = (salario_minimo * 10) / 100
    salario_inicial4 = horas * valor4
    print("Valor da hora trabalhada para a categoria O e turno N: R${}".format(valor4))
    print("O salário inicial desse funcionário é de R${}".format(salario_inicial4))