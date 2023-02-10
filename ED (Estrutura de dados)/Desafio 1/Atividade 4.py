# rescrever a Atividade 3 usando apenas uma lista

Dados: None= []

def inprimirDados() -> None:
    for i in range(3):
        print(f'Ola {Dados[i][0]}, Voce tem {Dados[i][1]} anos')

def pegarDados() -> None:

    for i in range(0, 3):
        Dados.append([input(f'Qual é o {i+1}º nome: '), int(input(f'Qual a {i+1}ª idade: '))])

    inprimirDados()

pegarDados()