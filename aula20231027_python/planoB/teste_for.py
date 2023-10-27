saldo = 1000  # Valor inicial
n = 6  # Número de meses
juros = 0.10  # Juros mensal 1% = 1/100 = 0.01

for mes in range(1, n + 1):
    saldo *= 1 + juros
    print(f"Mês ({mes}): {saldo:7.2f}")


x = 5
print(x)
x +=1
print(x)
x = x + 1
print(x)
