cont = 0
pares = 0
impares = 0
acm = 0
acmp = 0
for numero in range(1, 11):
    numero = int(input("Informe um número: "))
    cont = cont + 1
    acm = acm + numero
    media = acm / 10
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if numero % 2 == 0:
        acmp = acmp + numero
        pares = pares + 1
        mediapares = acmp / pares
    else:
        impares = impares + 1
        porcentagem = (impares / 10) * 100
print("A soma dos valores digitados é de {}".format(acm))
print("No total foram digitados 10 números")
print("A média dos números digitados foi de {}".format(media))
print("O maior número digitado foi {}".format(maior))
print("O menor número digitado foi {}".format(menor))
print("A média dos números pares é de {:.2f}".format(mediapares))
print("A porcentagem dos números ímpares entre os números digitados é de {:.1f}%".format(porcentagem))