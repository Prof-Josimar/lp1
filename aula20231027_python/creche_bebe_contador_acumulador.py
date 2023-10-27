##  Juarez pg 52
#continuar = input("Deseja começar (S/N): ").upper()
continuar = "S"
total_feminino = 0
soma_idade_feminino = 0
somatorio_mensalidade = 0.0
qtd_maior_18 = 0
media_idade_feminino = 0.0

while continuar != "N":
    sexo = input("Digite o sexo do bebê : ").upper()
    idade = int(input("Digite a idade do bebê em meses : "))
    valor_mesalidade = float(input("Digite o valor da mensalidade : "))

    if sexo == "F":
        print("Menina")
        total_feminino += 1
        soma_idade_feminino = soma_idade_feminino + idade

    else:
        print("Menino")
        somatorio_mensalidade = somatorio_mensalidade + valor_mesalidade

    if idade > 18:
        print("Maior de 18")
        qtd_maior_18 += 1

    continuar = input("Continuar 'S' ou 'N': ").upper()
    
if  total_feminino > 0:
    media_idade_feminino = soma_idade_feminino / total_feminino

print("-" * 40)
print("Media das idades das meninas.....: %.2f " % media_idade_feminino)
print("Total das mensalidades...........: %.2f " % somatorio_mensalidade)
print("Quantidade de bebes + 18 meses...: %d " % qtd_maior_18)
print("-" * 40)
print("total_feminino : ", total_feminino)
print("soma_idade_feminino ", soma_idade_feminino)
