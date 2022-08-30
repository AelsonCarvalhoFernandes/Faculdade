'''
6. Em outra tabela, o National Health and Nutrition Examination Survey (NHNES),
classifica-se homens de mulheres de modo diferente de acordo com o IMC:
Homens:
a) abaixo do peso ideal – IMC abaixo de 20,7
b) no peso ideal – IMC entre 20,8 e 27,8
c) acima do peso ideal – IMC entre 27,9 e 31,1
d) obeso – IMC acima de 31,1
a) abaixo do peso ideal – IMC abaixo de 19,1
b) no peso ideal – IMC entre 19,2 e 27,3
c) acima do peso ideal – IMC entre 27,4 e 32,3
d) obeso – IMC acima de 32,3
Escreva um algoritmo e um DFD que solicite ao usuário, o sexo, o peso e a altura e
classifique-o de acordo com esta nova tabela
'''

classificacao = int(input('[1] Homem, [2] Mulher'))
peso = float(input('Qual seu peso: Kg '))
altura= float(input('Qual a sua altura: M '))
imc= peso/(altura**2)

if classificacao == 1:
    if imc < 20.7:
        print(f'Esta abaixo do peso ideal. IMC = {imc}')
    elif imc >=20.8 and imc <= 27.8:
        print(f'Esta com o peso ideal. IMC = {imc}')
    elif imc > 27.9 and imc <= 31.1:
        print(f'Esta acima do peso. IMC = {imc}')
    elif imc > 31.1:
        print(f'Esta obeso. IMC = {imc}')
elif classificacao == 2:
    if imc < 19.1:
        print(f'Esta abaixo do peso ideal. IMC = {imc}')
    elif imc >=19.2 and imc <= 27.3:
        print(f'Esta com o peso ideal. IMC = {imc}')
    elif imc > 24.4 and imc <= 32.3:
        print(f'Esta acima do peso. IMC = {imc}')
    elif imc > 32.3:
        print(f'Esta obeso. IMC = {imc}')