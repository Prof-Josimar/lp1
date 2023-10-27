contF = 0
contM = 0
matricula = int(input("Digite a matricula : "))
while matricula != 999:
    n1 = float(input("Digite a nota 1 : "))
    n2 = float(input("Digite a nota 2 : "))
    n3 = float(input("Digite a nota 3 : "))
    sexo = input("Sexo : ").upper()
    if sexo[0] == "F":
        contF +=1
    else:
        contM +=1


    media = (n1 + n2 + n3) / 3
    print('Sua média.........: {:.2f}'.format(media))
    if (media < 6):
        print("Voce está Reprovado")
    else:
        print("Voce está  Aprovado")
    print("_"*40)
    matricula = int(input("Digite a matricula : "))


total_pessoas = contF + contM
percF = contF / total_pessoas * 100
percM = contM / total_pessoas * 100
print('Precentual homens....: {:.2f}'.format(percM) +"%")
print('Precentual mulheres..: {:.2f}'.format(percF)+ "%")
