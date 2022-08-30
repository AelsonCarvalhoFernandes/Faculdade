'''
9. Uma livraria oferece descontos de: 10% para professores, 15% para estudantes, 12%
para clientes fidelizados e 18% para funcionários. Todos os descontos não são
cumulativos. Escreva um algoritmo e um DFD que solicite ao usuário que informe a
qual das categorias pertence ou se não pertence a nenhuma delas, o preço do livro e
informe o valor da compra, o valor do desconto e o total a pagar.
'''

clientes = 0
clientesF = 0.12
Estudantes = 0.15
Professores = 0.10
funcionarios = 0.18

tipo = int(input('[1] Clientes\n[2] Clientes Fidelizados\n[3] Estudantes\n[4] Professores\n[5] Funcionários'))
Preço = float(input('Qual o preço do livro:\nR$ '))

if tipo == 1:
    Total = Preço
    print(f'O total a pagar é R${Total}')
elif tipo == 2:
    desconto = Preço*clientesF
    Total = Preço - desconto
    print(f'O total a pagar é R${Total}')
elif tipo == 3:
    desconto = Preço*Estudantes
    Total = Preço - desconto
    print(f'O total a pagar é R${Total}')
elif tipo == 4:
    desconto = Preço*Professores
    Total = Preço - desconto
    print(f'O total a pagar é R${Total}')
elif tipo == 5:
    desconto = Preço*funcionarios
    Total = Preço - desconto
    print(f'O total a pagar é R${Total}')
else:
    print('Tipo de cliente inválido!')