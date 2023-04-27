#O restaurante a quilo Bem-Bão cobra R$19,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e escreva o valor a pagar. Assuma que a balança já desconte o peso do prato.
Peso_Prato = float(input('Digite o peso do prato em quilograma: '))
valor = Peso_Prato * 19

print('O peso do prato foi de {} kg, e o preco ficou em {} reais. '.format(Peso_Prato,valor))

