'''
Uma empresa remunera seus funcionários 
por hora trabalhada.
Cada funcionário possui um valor específico 
por hora.
Nenhum funcionário recebe menos que 1 
salário mínimo.
Elabore um algoritmo que, dado o nome do 
funcionário, seu valor por hora e a sua qtde. 
de horas trabalhadas, calcule o valor do 
salário de um funcionário.
'''
from sre_compile import isstring
from os import error
import datetime


ligado = True # Controle que mantem o programa rodando

print('################################################################')
print('####################### Calcula salário ########################')
print('################################################################\n')


# Funções -----------------------------------------------------------------------------------------------------

def Calculo(valorHoras, horas) -> float: # Função que calcula o valor do salário do funcionário.
    try:
        total = valorHoras * horas
    except:
        print('Algum dos valores está inválido\n')
    finally:
        if total < 1200:
            total = 1200
            return total
        else:
            return total

def ajuda():
    escolha = input('''
[1] Como usar o programa.\n
[2] Como o Calculo é feito
:''')
    match escolha:
        case '1':
            print('''
Nome: Tem que ser um texto. não pode conter números ou caracteres especiais como @ # etc.\n

Valor da hora: O unico requisito é ser um numero. não coloque R$ ou $, letras ou qualquer outro caracterer especial.\n

Quantidade de horas: Digite um número inteiro. Não coloque letras ou caracteres especial.\n
            ''')
        
        case '2':
            print('O programa multiplica o valor da horas do funcionário pela quantidade de horas trabalhadas. Se o resultado for inferior a 1 salário minimo então automaticamente o valor vai ser igual a R$1200,00 \n')

#--------------------------------------------------------------------------------------------------------------

while ligado:
    start = input('Deseja fazer uma consulta ? [S] Sim [N] Não [A] Ajuda: ')


    if start == 's' or start == 'S':
        try: # Tratamento de erros gerais
            nome = input('Digite o nome do funcionário: ')

            if nome == None:
                print('O nome não pode está vazio.\n')
                erro = input('Deseja ver a ajuda, [S] Sim [N] Não :')
                if erro == 'S' or erro == 's':
                    ajuda()
            elif '!' in nome or '@' in nome or '#' in nome or '$' in nome or '%' in nome or '¨' in nome or '&' in nome or '*' in nome or '(' in nome or ')' in nome or '-' in nome or '_' in nome or '=' in nome or '+' in nome or '\\' in nome or ',' in nome or '.' in nome or '<' in nome or '>' in nome or ';' in nome or ':' in nome or '/' in nome or '?' in nome or '|' in nome or '[' in nome or ']' in nome or '{' in nome or '}' in nome:
                print('O nome não pode conter caracteres especiais.\n')
                erro = input('Deseja ver a ajuda, [S] Sim [N] Não :')
                if erro == 'S' or erro == 's':
                    ajuda()

            elif nome.isnumeric() == True:
                print('O nome não pode conter números.\n')
                erro = input('Deseja ver a ajuda, [S] Sim [N] Não :')
                if erro == 'S' or erro == 's':
                    ajuda()
            else:
                try: #tratamento de erros dos valores numericos
                    valorhoras = input('Digite o valor da hora: R$')
                    if ',' in valorhoras:
                        valorhoras = float(valorhoras.replace(',', '.'))
                        
                        quanthoras = int(input('Digite a quantidade de horas inteiras: '))

                        valor_total = Calculo(valorhoras, quanthoras)
                        print(f'O funcionário {nome} vai receber R${valor_total:.2f}')
                    else:
                        valorhoras = float(valorhoras)
                    
                        quanthoras = int(input('Digite a quantidade de horas inteiras: '))

                        valor_total = Calculo(valorhoras, quanthoras)
                        print('O funcionário {} vai receber R${}'.format(nome, valor_total))
                        
                except error as ex:
                    log = open('log.txt' 'w')
                    log.write(error, ':',datetime.datetime.now)
                    print('O valor informado está errado.\n')
                    erro = input('Deseja ver a ajuda, [S] Sim [N] Não :')
                    if erro == 'S' or erro == 's':
                        ajuda()
        except error as ex:
            log = open('log.txt' 'w')
            log.write(error, ':', datetime.datetime.now)
            print('Algo de errado não esta certo!!')
            erro = input('Deseja ver a ajuda, [S] Sim [N] Não :')
            if erro == 'S' or erro == 's':
                ajuda()
            
    
    if start == 'n' or start == 'N':
        ligado = False
    if start == 'a' or start == "A":
        ajuda()