'''Crie um programa que faça a tabuada de um número qualquer
inteiro que será digitado pelo usuário, número inteiro
entre 1 a 10. O usuário deve informar de qual numero ele
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:'''

num = int(input('Digite um número de 1 a 10 e descubra sua tabuada:'))
if num >= 1 and num <= 10:
    for i in range(1,10):
        tabuada = num * i
        print(num,'x',i,'=',tabuada)