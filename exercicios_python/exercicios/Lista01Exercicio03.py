Custo_Fabrica = float(input('Digite o custo de fabricado carro: '))

Margem_distribuidor = 0.28
Imposto = 0.45

Custo_Consumidor = Custo_Fabrica + (Custo_Fabrica*Margem_distribuidor) + (Custo_Fabrica*Imposto)

print(Custo_Consumidor)
