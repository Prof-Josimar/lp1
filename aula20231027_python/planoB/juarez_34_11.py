
n1 = int(input("Digite o primeiro numero : "))
n2 = int(input("Digite o segundo numero : "))
n3 = int(input("Digite o terceiro numero : "))

if n1 > n2 and n1 > n3:
    print(n1)
    if n2 > n3:
        print(n2, "\n", n3)
    else:
        print(n3, "\n", n2)
elif n2 > n1 and n2 > n3:
    print(n2)
    if n1 > n3:
        print(n1, "\n", n3)
    else:
        print(n3, "\n", n1)

else:
    if n3 > n1 and n3 > n2:
        print(n3)
        if n1 > n2:
            print(n1, "\n", n2)
        else:
            print(n2, "\n", n1)
