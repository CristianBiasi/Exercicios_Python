#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.
P = int(input('Digite a quatidade de camisetas P vendidas: '))
M = int(input('Digite a quatidade de camisetas M vendidas: '))
G = int(input('Digite a quatidade de camisetas G vendidas: '))
soma = (P*10) + (M*12) + (G*15)
print('O valor arrecado com a venda das camisetas P,M e G totalizaram em Reais', soma)
