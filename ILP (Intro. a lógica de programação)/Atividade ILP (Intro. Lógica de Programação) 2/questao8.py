'''
8. Escreva um programa e um DFD no qual o usuário digitará o dia, o mês (como
inteiro) e ano e o programa exibirá uma data com o mês em extenso. Exemplo:
Dia: 10
Mês: 8
Ano: 2013
O programa exibirá:
10 de Agosto de 2013
'''

meses = ['Janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

dia= int(input('Digite o dia: '))
mes = int(input('Digite o numero do mês: '))
ano = int(input('Digite o ano: '))

print(f'{dia} de {meses[mes-1]} de {ano}')
