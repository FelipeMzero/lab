from math import tan, pi

lados = 5
comprimentos = []
for i in range(lados):
    comprimento = float(input(f"Digite o comprimento do lado {i+1}: "))
    comprimentos.append(comprimento)

regiao = input("Digite a região (centro, area nobre ou periferia): ")
if regiao == "centro":
    valor_metro_quadrado = 130
elif regiao == "area nobre":
    valor_metro_quadrado = 200
else:
    valor_metro_quadrado = 80

area_total = 0.25 * (lados * sum(comprimentos) ** 2) / (tan(pi / lados))
preco = area_total * valor_metro_quadrado
print(f"A área total do terreno é: {area_total:.2f} metros quadrados")
print(f"O preço do terreno é: R$ {preco:.2f}")
