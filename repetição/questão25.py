cont = 0 
n = int(input("Digite um número:"))
c = n * cont 
for c in range(0,11):
    cont = cont + 1
    print("O cálculo de {} * {} = {}".format( n, cont, n * cont))