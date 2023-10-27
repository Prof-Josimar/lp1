def linha():
    for i in range(30):
        print("_", end="")
    print("\n")


for i in range(3):
    nome = input("Digite seu nome : ")
    salarioBruto = float(input("Digite o salario : "))
    valorDesconto = salarioBruto * (8 / 100)
    salarioLiquido = salarioBruto - valorDesconto
    print("O desconto foi ", valorDesconto)
    print("O salario liquido é ", salarioLiquido)
    linha()
    
# esta indentação termina o loop




