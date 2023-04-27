#Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.
vendedor = str(input('Digite o nome do vendedor: '))
SalarioFixo = float(input('Digite o salario fixo: '))
VendasTotal = float(input('Digite o total de vendas em dinheiro: '))
comissao = VendasTotal * 1.15
SF = SalarioFixo + comissao
print('{}, seu salario fixo é de {}, mais a comissao de suas vendas, seu salario final é de {}, Parabens! '.format(vendedor,SalarioFixo,SF))
