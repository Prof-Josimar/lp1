# Defina o número
numero = 386

# Calcule as centenas, dezenas e unidades
centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

# Imprima os resultados
print(f"{centenas} centenas, {dezenas} dezenas, {unidades} unidades")
