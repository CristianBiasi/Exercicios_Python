Distancia_Percorrida = float(input('Digite a distancia total percorrida em quilometros: '))
Combustivel_Gasto = float(input('Digite o gasto total de combustivel em Litros: '))

Consumo_Medio = Distancia_Percorrida / Combustivel_Gasto

# Maneira comum de dar o print
# print('O consumo medio de combustivel é de: ',Consumo_Medio,'Km/L')

print('O consumo medio de combustivel é de {} KM/L'.format(Consumo_Medio))

