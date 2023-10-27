
letra = input("Digite uma letra : ").upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("É vogal")
else:
    print("Não É vogal")


# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ")

# Certifica-se de que o usuário digitou apenas um caractere
if len(letra) == 1:
    # Converte a letra para minúscula para facilitar a comparação
    letra = letra.lower()

    # Verifica se a letra é uma vogal
    if letra in 'aeiou':
        print(f'A letra "{letra}" é uma vogal.')
    else:
        print(f'A letra "{letra}" é uma consoante.')
else:
    print("Por favor, digite apenas uma letra.")
