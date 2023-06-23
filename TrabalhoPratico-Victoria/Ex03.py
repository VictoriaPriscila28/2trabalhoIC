''' Um palíndromo é uma sequência de caracteres
 cuja leitura é idêntica se feita da direita para
 esquerda  ou  vice−versa.
 Por  exemplo: OSSO e OVO são  palíndromos.
 Crie um  programa que leia uma seqüência de
 caracteres, mostre−a e diga se é um palíndromo ou não.'''
str = str(input('Digite uma palavra e descubra se ela é um políndromo:')).strip().upper()

if str == str[::-1]:
    print('É um políndromo!')
else:
    print('Infelizmente não é!')


