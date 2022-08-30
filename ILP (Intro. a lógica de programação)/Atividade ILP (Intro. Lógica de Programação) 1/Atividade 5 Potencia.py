'''
19) Faça um DFD e um programa em python
que receba 2 números e informe a potência
(um elevado ao outro) utilizando apenas
somas.
'''
# Entrada de usuário
n1 = int(input('Digite a base:'))
n2 = int(input('Digite a potencia:'))

res1 = n1
res2 = n1

if n1 != 0 and n2 != 0 and n2 != 2:
    for c1 in range(1, n2):
        for c2 in range(1, n1):
            res1 += res2
        res2 = res1
elif n2 == 2:
    for c1 in range(1, n2):
        for c2 in range(1, n1):
            res1 += res2
        res2 = res1

print("O valor de {} elevado a {} é {}".format(n1, n2, res1))




