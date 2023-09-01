feminino = 0
masculino = 0
contexperiencia = 0
sexo = 0
idade21 = 0
expfeminino = 0
acm = 0
media = 0

for i in range(1, 5):
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo [M/F]"))
    experiencia = str(input("Teve experiência? [S/N]"))
    if sexo == 'F':
        feminino = feminino + 1
        expfeminino = expfeminino + 1
        if experiencia == 'S':
            if expfeminino == 1:
                menor = idade
            else:
                if idade < menor:
                    menor = idade
    elif sexo == 'M':
        masculino = masculino + 1
    if experiencia == 'S' and sexo == 'M':
        contexperiencia = contexperiencia + 1
        acm = acm + idade
        media = acm / contexperiencia
    if sexo == 'M' and idade > 45:
        sexo = sexo + 1
    porcentagem = (sexo / 4) * 100
    if sexo == 'F' and idade < 21 and experiencia == 'S':
        idade21 = idade21 + 1

print("{} candidatas são do sexo feminino".format(feminino))
print("{} candidatos são do sexo masculino".format(masculino))
print("A idade média dos homens que já tem experiência no serviço é de {}".format(media))
print("{}% dos homens candidatados tem mais de 45 anos".format(porcentagem))
print("{} mulheres tem idades inferiores a 21 anos e têm experiência no serviço".format(idade21))
print("A menor idade entre as mulheres que já têm experiência no serviço é de {} anos".format(menor))