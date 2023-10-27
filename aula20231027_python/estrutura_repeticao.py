desconto = 0.0
salario_liquido = 0.0
for i in range(3):
    print("")
    matricula = input("Digite a matricula do funcionário...: ")
    salario_bruto = float(input("Digite o salario....................: "))

    desconto = salario_bruto * 8 / 100
    salario_liquido = salario_bruto - desconto

    print('O salario liquido é.................: {:.2f}'.format(salario_liquido))
    print('O desconto foi......................: {:.2f}'.format(desconto))
    print("_"*50)
