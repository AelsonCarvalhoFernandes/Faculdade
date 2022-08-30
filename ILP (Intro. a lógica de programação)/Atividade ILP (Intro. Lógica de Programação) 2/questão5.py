'''
5. De acordo com índice de massa corporal (de acordo com a Organização Mundial de
Saúde), uma pessoa pode ser classificada como:
a) abaixo do peso ideal – IMC abaixo de 18,5
b) no peso ideal – IMC entre 18,5 e 25
c) acima do peso ideal – IMC entre 25,1 e
30 d) obeso – IMC acima de 30

Sabendo que o IMC pode ser calculado como o peso (em quilos) dividido
quadrado da altura (metros), escreva um algoritmo e um DFD que solicite o peso e
a altura de um usuário e classifique-o de acordo com estes dados
'''

peso = float(input('Qual seu peso: Kg '))
altura= float(input('Qual a sua altura: M '))
imc= peso/(altura**2)

if imc < 18.5:
    print(f' {imc}')
elif imc >=18.5 and imc <= 25:
    print(f'Esta com o peso ideal. IMC = {imc}')
elif imc > 25 and imc <= 30:
    print(f'Esta acima do peso. IMC = {imc}')
elif imc > 30:
    print(f'Esta obeso. IMC = {imc}')