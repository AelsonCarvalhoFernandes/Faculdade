'''
7. Imagine que em uma barraca de cachorro quente, cada cachorro quente custe R$4,00.
Um copo de refrigerante custa R$ 2,00. A cada três cachorros quentes, ganha-se
gratuitamente 1 refrigerante ou R$1,00 de desconto. Escreva um programa e um DFD
que solicite ao usuário a quantidade de cachorros quentes, a quantidade de
refrigerantes e diga ao usuário qual deve ser o total a pagar, considerando os
descontos dos refrigerantes gratuitos. Exemplos:

'''
import math
cachorroquente = 4.00
refrigetante = 2.00

totalapagar = 0

quantcachorro = int(input('Quantos cachorro quentes deseja'))
quantrefrigerante = int(input('Quantos refrigerantes deseja'))

desconto = 0
descontoemreais= 0

if quantcachorro > 3 :
    desconto = 1*math.floor(quantcachorro/3)
    if quantrefrigerante > 0:
        quantrefrigerante = quantrefrigerante - desconto
        totalapagar = (quantcachorro*cachorroquente)+(quantrefrigerante*refrigetante)
    else:
        descontoemreais = 1.00(math.floor(quantcachorro/3))
        totalapagar = (quantcachorro*cachorroquente)-descontoemreais
else:
    totalapagar = (quantcachorro*cachorroquente)+(quantrefrigerante*refrigetante)
    
print(totalapagar)
    
    