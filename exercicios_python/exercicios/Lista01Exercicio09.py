abastecimento = float(input('Digite o valor R$ do abastecimento em reais: '))
gasolina = float(input('Digite o valor do litro da gasolina: '))
litros = abastecimento / gasolina
# Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
print('O valor da gasolina hoje é de {:.2f} e o valor do pagamento ficou em R${:.2f}, com essa quantia voce abasteceu {:.2f} litros de gasolina no seu carro: '.format(gasolina,abastecimento,litros))
