import requests
import json

requisição = requests.get('https://economia.awesomeapi.com.br/all')
cotação_moeda = requisição.json()
print('-----------------------------')
print('Software para pegar a cotação')
print('-----------------------------\n\n')
print('Nome | Tipo de cotação\n')
for i in cotação_moeda:
    print(cotação_moeda[i]['code'], '|',cotação_moeda[i]['name'], '\n')

escolha = (input('Qual a cotação deseja pegar: '))

print('-------------------------------------------------------------')
print('moeda:: ', {cotação_moeda['{}'.format(escolha)]['name']})
print('data: ' + cotação_moeda['{}'.format(escolha)]['create_date'])
print('O valor atual: R$' + cotação_moeda['{}'.format(escolha)]['bid'])
print('-------------------------------------------------------------')