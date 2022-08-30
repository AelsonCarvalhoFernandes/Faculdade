'''
2. Um ano é bissexto se for múltiplo de 4 e não for múltiplo de 100, ou for múltiplo de
400. Escreva um algoritmo e um DFD que receba um ano como entrada e diga se o
ano é ou não bissexto.
'''
ano = int(input('Digite o ano:'))

if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0:
    print('O ano informado é bisexto')
else:
    print('O ano não é bisexto')