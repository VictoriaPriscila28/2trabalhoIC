'''Crie um programa que solicita as quatro notas de 10 alunos,
calcule e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0'''
import statistics
lista = list()
listacomposta = list()
media = 0
for c in range(11):
    for i in range(0,4):
        listacomposta.append(float(input(f'Digite a {i+1}º nota:')))
    media = statistics.mean(listacomposta)
    print('Sua média: ',media)
if media >= 7:
            print('Sua média foi acima de 7,0 :', media)
else:
            print('Sua média foi abaixo de 7,0 :', media)
lista.clear()






