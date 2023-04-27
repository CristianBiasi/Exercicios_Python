#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
produto = float(input('Digite o valor do produto: '))
prestaçoes = int(input('Digite a quantidade de prestacoes: '))
compra = produto / 5

print('Voce adquiriu o produto X no valor de {}, e dividiu em um total de {} prestacoes, e cada prestacao ficou no valor de {}. '.format(produto,prestaçoes,compra))
