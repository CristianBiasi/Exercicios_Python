#Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.
deposito = float(input('Digite o valor do deposito: '))
juros = 0.7 / 100
ValorRendimento = deposito * (1 + juros)
print("O valor com rendimento após um mês é: R$", round(ValorRendimento, 2))
