valor_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (rendimentos) em %: "))
meses = int(input("Digite a quantidade de meses que pretende investir: "))
valor_total = valor_inicial

for mes in range(1, meses + 1):
    print(f"Mês {mes}:")
    print(f"Saldo no início do mês: R$ {valor_total:.2f}")
    
    depositar = input("Deseja fazer um depósito neste mês? (S/N): ").upper()
    if depositar == "S":
        valor_deposito = float(input("Digite o valor do depósito: "))
        valor_total += valor_deposito
    
    juros_mensais = valor_total * (taxa_juros / 100)
    valor_total += juros_mensais
    
    print(f"Saldo após juros: R$ {valor_total:.2f}")
    print()

retorno_investimento = valor_total - valor_inicial
print(f"Valor total ganho com juros no período: R$ {retorno_investimento:.2f}")
