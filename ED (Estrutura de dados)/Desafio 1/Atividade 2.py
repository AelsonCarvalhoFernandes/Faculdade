# Reescrever a atividade 1 usando funções

def inprimirDados(nome: str, idade: int) -> None:
    print(f'Ola {nome}, Voce tem {idade} anos')

def pegarDados() -> None:
    nome: str = input('Qual é o seu nome: ')
    idade: int = int(input('Qual a sua idade: '))

    inprimirDados(nome, idade)

pegarDados()