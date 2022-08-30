'''
11. Considere uma lanchonete com as seguintes opções de bebidas, lanches e preços:
Lanches:
a) Hamburguer – R$ 4,00
b) X-Burguer – R$ 5,00
c ) Misto – R$ 4,50
Bebidas:
a) Suco de Laranja – R$ 3,50
b) Suco de Abacaxi – R$ 3,00
c) Refrigerante – R$ 2,50
d) Água Mineral – R$ 2,00
Escreva um programa e um DFD que solicite ao usuário o tipo de lanche, a
quantidade, o tipo de bebida e a quantidade e por fim exiba o pedido e o total a pagar.
'''
# Valor
lanche = 0.00
bebidas = 0.00

# Lanches
hamburguer = 4.00
xburguer = 5.00
misto = 4.50
escolhalanches= int(input('Digite qual lanche deseja.\n[1] Hamburguer\n[2] X-Burguer\n[3] Misto\n[4] Nenhum'))
if escolhalanches == 1:
    quantlancher = int(input('Qual a quantidade de lanches deseja: '))
    lanche = hamburguer*quantlancher
elif escolhalanches == 2:
    quantlancher = int(input('Qual a quantidade de lanches deseja: '))
    lanche = xburguer*quantlancher
elif escolhalanches == 3:
    quantlancher = int(input('Qual a quantidade de lanches deseja: '))
    lanche = misto*quantlancher
elif escolhalanches == 4:
    pass

# Bebidas
sucolaranja = 3.50
sucoabacaxi = 3.00
refrigerante = 2.50
aguamineral = 2.00

escolhabebidas= int(input('Qual bebida deseja.\n[1] Suco de laranja\n[2] Suco de abacaxi\n[3] Refrigerante\n[4] Água Mineral\n[5] Nenhum'))

if escolhabebidas == 1:
    quantbebidas = int(input('Qual a quantidade de bebidas deseja: '))
    bebidas = sucolaranja*quantbebidas
if escolhabebidas == 2:
    quantbebidas = int(input('Qual a quantidade de bebidas deseja: '))
    bebidas = sucoabacaxi*quantbebidas
if escolhabebidas == 3:
    quantbebidas = int(input('Qual a quantidade de bebidas deseja: '))
    bebidas = refrigerante*quantbebidas
if escolhabebidas == 4:
    quantbebidas = int(input('Qual a quantidade de bebidas deseja: '))
    bebidas = aguamineral*quantbebidas
if escolhabebidas == 5:
    pass

total = lanche + bebidas

print(f'O valor total a pagar é R${total:.2f}')
    