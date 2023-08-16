num_funcionarios = int(input("Digite o número de funcionários na empresa: "))

for i in range(num_funcionarios):
    salario_inicial = float(input(f"Digite o salário do funcionário {i+1}: "))
    aumento = salario_inicial * 0.15
    salario_com_aumento = salario_inicial + aumento
    desconto_impostos = salario_com_aumento * 0.08
    salario_final = salario_com_aumento - desconto_impostos
    
    print(f"Funcionário {i+1}:")
    print(f"Salário inicial: R$ {salario_inicial:.2f}")
    print(f"Salário com aumento: R$ {salario_inicial * 1.15:.2f}")
    print(f"Salário final após desconto de impostos: R$ {salario_final:.2f}")
    print()
