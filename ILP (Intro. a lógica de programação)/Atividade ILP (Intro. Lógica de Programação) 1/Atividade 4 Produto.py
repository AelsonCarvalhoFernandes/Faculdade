n1 = int(input('Digite um numero:\n'))
n2 = int(input('Digite outro numero:\n'))
multi = 0
for i in range (0, n2):
   multi += n1
   print('O produto entre {} e {} é {}'.format(n1, n2, multi))