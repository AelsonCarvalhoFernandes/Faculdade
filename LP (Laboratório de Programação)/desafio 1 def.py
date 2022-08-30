# Variaveis e lista -------------------------------------------------------------------------------------------
from pickle import TRUE


on = True # Mantem o programa ligado
# Funções -----------------------------------------------------------------------------------------------------
def ajuda():
    print('''
Calculo: O calcuco é a multiplicação do valor da hora pela quantidade de horas trabalhadas.
Nome: Não pode conter caracteres especiais ou numeros.
Valor da hora: Coloque apenas o valor sem o R$ ou qualquer caracteres especiais.
Quantidade de horas: Primeiro digite a quantidade de horas e depois a quantidade de minutos sem caracteres especiais.
    ''')
def tratar_nome(n):
    nome = n
    try:
        if '!' in nome or '@' in nome or '#' in nome or '$' in nome or '%' in nome or '¨' in nome or '&' in nome or '*' in nome or '(' in nome or ')' in nome or '-' in nome or '_' in nome or '=' in nome or '+' in nome or '\\' in nome or ',' in nome or '.' in nome or '<' in nome or '>' in nome or ';' in nome or ':' in nome or '/' in nome or '?' in nome or '|' in nome or '[' in nome or ']' in nome or '{' in nome or '}' in nome or '1' in nome or '2' in nome or '3' in nome or '4' in nome or '5' in nome or '6' in nome or '7' in nome or '8' in nome or '9' in nome or '0' in nome:
            escolha = input('O nome não pode conter caracteres especiais ou numeros.\n Deseja ver a ajuda: [S] Sim [Enter] Não:')
            if escolha == 'S' or escolha == 's':
                ajuda()
        else:
            return nome
    except:
        escolha = input('O nome não pode conter caracteres especiais ou numeros.\n Deseja ver a ajuda: [S] Sim [Enter] Não:')
        if escolha == 'S' or escolha == 's':
            ajuda()
def tratar_valor(v): # 
    valor = str(v)
    try:
        if ',' in valor:
            valor = valor.replace(",", ".")
            valor = float(valor)
            return valor
        else:
            valor = float(valor)
            return valor
    except:
        escolha = input('O valor não pode conter caracteres especiais ou letras.\n Deseja ver a ajuda: [S] Sim [Enter] Não:')
        if escolha == 'S' or escolha == 's':
            ajuda()
def tratar_horas(h, m): # Faz o tratamento da hora
    horas = h
    minutos = m
    try:
        horas = int(horas)
        minutos = int(minutos)
        minutos = ((minutos*100)/60)/100

        horastotal= horas + minutos
        return horastotal
    except:
        escolha = input('O valor da hora e minutos não pode conter caracteres especiais ou letras.\n Deseja ver a ajuda: [S] Sim [Enter] Não:')
        if escolha == 'S' or escolha == 's':
            ajuda()
# Inicio do programa ------------------------------------------------------------------------------------------
while on:
    escolha = input('Deseja fazer uma consulta? [S] Sim [N] Não [A] Ajuda:')
    if escolha == 'S' or escolha == 's':
        nome = tratar_nome(input('Digite o nome do funcionário:'))
        if nome !=None:
            valor = tratar_valor(input('Digite o valor da hora: '))
            if valor != None:
                horas = tratar_horas(input('digite a quantidade de horas trabalhadas:'), input('Digite a quantidade de minutos:'))
                if horas != None:
                    valortotal = valor*horas
                    if valortotal < 1212:
                        print(f'O funcionário {nome} vai receber R$1212,00')
                    else:
                        print(f'O funcionário {nome} vai receber R${valortotal:.2f}')
    elif escolha == "N" or escolha == "n":
        on = False
    elif escolha == "A" or escolha == "a":
        ajuda()
# Fim ---------------------------------------------------------------------------------------------------------