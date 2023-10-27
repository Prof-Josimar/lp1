nome = input("Digite uma palavra : ").lower()
vogais = 0
consoantes = 0
for i in nome:
    if i in "aeiou":
        vogais += 1
    else:
        consoantes += 1
print("Qtd vogais ", vogais)
print("Qtd conso ", consoantes)
