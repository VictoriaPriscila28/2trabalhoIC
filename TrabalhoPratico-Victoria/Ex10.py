''' Crie um programa que leia um número indeterminado de
valores, correspondentes a notas,
encerrando a entrada de dados quando for
informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:

a)Mostre a quantidade de valores
que foram lidos;
b)Exiba todos os valores na ordem em que foram informados;
c)Exiba todos os valores na ordem inversa à que foram informados;
d)Calcule e mostre a soma dos valores;
e)Calcule e mostre a média dos valores;
f)Calcule e mostre a quantidade de valores acima da média calculada;
g)Calcule e mostre a quantidade de valores abaixo de sete;
h)Encerre o programa com uma mensagem.'''

import statistics

lista = list()
listacomposta = list()
n = int(input('Digite qualquer número para prosseguir ou -1 para parar: '))

while n != -1:

    listacomposta.append(float(input('Digite sua nota: ')))
    n = int(input('Digite qualquer número para prosseguir ou -1 para parar: '))
    lista.clear()
    if n == -1:
     print('Calculando...')

media = statistics.mean(listacomposta)


print('A quantidade de notas digitadas foi de: ',len(listacomposta)) #a
print('Valores das notas de acordo com a ordem digitada: ',listacomposta) #b
lista.reverse()
print('Ordem inversa das notas:',listacomposta) #c
print('A soma de todas as notas é:',sum(listacomposta)) #d
print('A média aritmética entre as notas é de:',format(media)) #e
print('"Nós aqui sabemos o que deveríamos ter feito ontem,\n'
      'e sabemos o que devemos fazer amanhã,\n'
      'mas nunca sabemos o que devemos fazer hoje."-Lewis Carrol\n') #h





