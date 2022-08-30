'''
10. Determinada empresa de ônibus vende passagens para: Eunápolis, Camacã, Itabuna e
Itacaré. As passagens possuem o seguinte preço:
a) Eunápolis: R$4.00
b) Camacã: R$8.00
c) Itabuna: R$13.00
d) Itacaré: R$20.00
Escreva um algoritmo e um DFD que peça para o usuário digitar a letra
correspondente à cidade pra onde deseja viajar, a quantidade de passagens e diga
quanto ele deve pagar.
'''

Viagem = int(input('Digite para onde deseja ir:\n[1] Eunápolis\n[2] Camacã\n[3] Itabuna\n[4] Itacaré\nEscolha:'))
quant = int(input('Quantas passagem deseja:\n'))

valor = 0

if Viagem == 1:
    eunapolis = 4.00*quant
    valor = eunapolis
    print(f'O valor a pagar é R${valor:.2f}')  
elif Viagem == 2:
    camaca = 8.00*quant
    valor = camaca
    print(f'O valor a pagar é R${valor:.2f}')
elif Viagem == 3:
    itabuna = 13.00*quant
    valor = itabuna
    print(f'O valor a pagar é R${valor:.2f}')
elif Viagem == 4:
    itacare = 20.00*quant
    valor = itacare
    print(f'O valor a pagar é R${valor:.2f}')
else:
    print('Destino invalido')
    
