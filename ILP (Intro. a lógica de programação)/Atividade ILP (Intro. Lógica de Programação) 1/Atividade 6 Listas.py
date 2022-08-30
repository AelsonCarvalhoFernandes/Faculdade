print(
    '''
    Tente Adivinhas a fruta que estaá dentro da lista
    '''
)

lista = ['banana', 'abacaxi', 'maçã', "uva", 'manga']
chute = input('Qual fruta pode esta na lista: ')

for l in lista:
    if (chute == l):
        print('Acertou. Há {} na lista'.format(l))