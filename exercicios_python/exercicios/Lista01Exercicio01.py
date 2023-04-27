# Variaveis de espaço
PC = float(input('Digite o ponto de chegada em Km: '))
PP = float(input('Digite o ponto de partida em Km: '))

# Variaveis de tempo
TF = float(input('Digite o tempo final em Hrs: '))
TI = float(input('Digite o tempo inicial em Hrs: '))

#Variaveis Δ Delta
DS = PC - PP
DT = TF - TI

Vm = DS / DT

print(Vm)
