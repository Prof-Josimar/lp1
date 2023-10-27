TAM = 1

for i in range(TAM):
    matr = input(f"Digite a matricula do {(i+1)} .ª funcionario ")
    tot_vendas = float(input(f"Digite o total das vendas do {(i+1)} : "))
    com = tot_vendas * 3 / 100
    print("Comissão do {} .º funcionario  R$ {:.2f}".format(matr, com))
    print("_" * 40)


