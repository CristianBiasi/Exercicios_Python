#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança.
VendasPaoFrances = int(input('Digite a quantidade de paes vendidas. '))
Bolos = int(input('Digite a quantidade de bolos vendidas: '))
LucroPaoEbolo = (VendasPaoFrances * 0.12) + (Bolos * 1.5)
juntar = LucroPaoEbolo * 0.10

print('Foi arrecada com a venda dos Paes e Bolos a quantia de {}, e deste total voce devera guardar {:.2f} na sua poupanca'.format(LucroPaoEbolo,juntar))
