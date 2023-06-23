''' Uma academia deseja fazer um senso entre seus clientes
para descobrir o mais alto, o mais baixo, o que possui sobrepeso e o
mais magro. Para isto você deve criar um programa que pergunte a
cada um dos clientes da academia seu código, sua altura
e seu peso. O final da digitação  de  dados deve
ser dado quando  o  usuário  digitar  0  (zero)
no  campo  código.  Ao encerrar o programa também deve ser
 informado os códigos e valores do client emais alto,
 do mais baixo, do que possui sobrepeso e do mais magro,
 além da média das alturas e dos pesos dos clientes.'''
import statistics


altura = 0
peso = 0
lista = list()
listacomposta = list()
listacomposta2 = list()

n = int(input('Digite qualquer número para prosseguir ou 0 para parar: '))
while n != 0:

    listacomposta.append(float(input('Digite sua altura: ')))
    listacomposta2.append(float(input('Digite seu peso: ')))
    n = int(input('Digite qualquer número para prosseguir ou 0 para parar: '))
    altura = listacomposta
    peso = listacomposta2

    lista.clear()
    if n == 0:
        print('Calculando...')


mediana = statistics.median(listacomposta)
mediana2 = statistics.median(listacomposta2)

print('Alturas em ordem crescente:',sorted(listacomposta))
print('Pesos em ordem crescente:',sorted(listacomposta2))
print('O cliente mais alto mede:',max(listacomposta)) #a
print('O cliente mais baixo mede:',min(listacomposta)) #b
print('O cliente mais pesado pesa:',max(listacomposta2)) #c
print(f'O cliente de menor peso pesa:',min(listacomposta2)) #d
print('O valor médio das alturas é de:',format(mediana)) #e
print('O peso médio entre os clientes é de:',format(mediana2)) #f

























