Nome_Aluno = str(input('Digite o nome do aluno: '))

Prova1 = float(input('Digite a nota da primeira prova: '))
Prova2 = float(input('Digite a nota da segunda prova: '))
Prova3 = float(input('Digite a nota da terceira prova: '))

Media_Aritmética = (Prova1 + Prova2 + Prova3) / 3

print('O aluno(a) {} tirou na sua primeira prova {}, na segunda {}, e na terceira {}, e sua media aritmética foi de {:.2f}'.format(Nome_Aluno,Prova1,Prova2,Prova3,Media_Aritmética))
