deposito_inicial = float(input("Digite o valor do Depósito inicial: "))
juros = float(input("Informe o valor do juros: "))
valor_deposito_mensal = float(input("Digite o valor do depósito mensal: "))

for i in range(1, 25):
    deposito_inicial += valor_deposito_mensal 
    deposito_inicial += deposito_inicial * (juros / 100)  
    print(f"Mês {i}: R$ {deposito_inicial:.2f}")

total_ganho_juros = deposito_inicial - (deposito_inicial / (1 + juros / 100))
print(f"O valor total ganho com os juros = R$ {total_ganho_juros:.2f}")
