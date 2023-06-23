''' Crie um programa que leia uma lista com
10 números inteiros, calcule e
 mostre a soma dos quadrados dos elementos da lista.'''

lista = []
for i in range(0,10):
    lista.append(float(input(f'Digite o {i+1}º número:')))
print('Esses foram os números escolhidos:',lista)
print('A soma dos quadrados dos elementos da lista resulta em: {:.2f} '.format(sum(lista)**2))
