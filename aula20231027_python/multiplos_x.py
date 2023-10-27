num = int(input("Digite um numero : "))
for i in range(1,100):
    if (i % num == 0):
        print(i , " é multiplo de ",num)
    else:
        print(i , " Não  é multiplo de ",num)
