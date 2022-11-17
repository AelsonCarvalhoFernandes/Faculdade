from Data.Cadastrar import *

onof = True

while onof:
    escolha = input('Oque deseja fazer:\n[ 1 ] Cadastrar, [ 2 ] Consultar, [ 3 ] Atualizar, [ 4 ] Excluir')

    if escolha == '1':
        ps = Cadastrar()
        ps.cadastrarP('Joao', '3131242315', 22, '12/10/1995', 1220.00)
