#Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
preco_custo = float(input("Digite o preço de custo do produto: "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo desejado (exemplo: 10 para 10%): "))

preco_venda = preco_custo * (1 + percentual_acrescimo/100)

print(f"O preço de venda do produto será R${preco_venda:.2f}")
