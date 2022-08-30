'''
Escreva um algoritmo e um DFD que receba 3 números como entrada e exiba-os em
ordem crescente.
'''

n1= int(input('Digite 3 numeros:\n'))
n2=int(input())
n3=int(input())

no_order= [n1, n2, n3]

order = sorted(no_order)

print(f'A sequencia de numeros ordenadas é {order}')

