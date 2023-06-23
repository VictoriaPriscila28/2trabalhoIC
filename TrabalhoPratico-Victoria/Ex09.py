''' Crie um programa que solicita a idade e a altura de 5 pessoas,
armazene cada informação em uma lista.
Imprima a idade e a altura na ordem inversa a ordem lida.'''

idade = 0
altura = 0
lista = list()
listacomposta = list()
for i in range(0,5):
    lista.append(float(input(f'Digite a {i+1}° altura:')))
    lista.append(int(input(f'Digite a {i+1}° idade:')))
    listacomposta.append(lista[:])
    idade += listacomposta[i][1]
    altura += listacomposta[i][1]
    lista.clear()

print('Valores das alturas e idades de acordo com a ordem digitada:',listacomposta)
print('Valores das alturas e idades de acordo com a ordem crescente:',sorted(listacomposta))
listacomposta.reverse()
print('Ordem inversa das alturas e idades:',listacomposta)
