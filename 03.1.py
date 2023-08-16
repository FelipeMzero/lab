quantidade_de_frangos = int(input("\nDigite a quantidade de frangos: "))

tipo_de_racao = int(input("Informe o tipo de ração: \n1 - Tipo A ou 2 - Tipo B: "))

anel_indentificacao = quantidade_de_frangos * 4
anel_alimento = quantidade_de_frangos * (3.50*2)
valor_do_frango = anel_alimento + anel_indentificacao

if tipo_de_racao == 1:
    novo_valor = valor_do_frango * 0.20
    valor_consumo_final = novo_valor + valor_do_frango
    print("O gasto com a quantidade de frango(s) com a ração de tipo",tipo_de_racao,"é de R$:",valor_consumo_final)
elif tipo_de_racao == 2:
    novo_valor = valor_do_frango * 0.14
    valor_consumo_final = novo_valor + valor_do_frango
    print("O gasto com a quantidade de frango(s) com a ração de tipo",tipo_de_racao,"é de R$:",valor_consumo_final)
else:
    print("Os dados informados estão errados")
    print()





