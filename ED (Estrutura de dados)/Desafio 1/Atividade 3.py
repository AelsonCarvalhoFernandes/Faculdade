# reescrever a atividade 2 usando lista para receber 3 nomes e outra lista para receber 3 idades

nomes: str = []
idade: int = []

def inprimirDados(nome: str, idade: int) -> None:
    print(f'Ola {nome}, Voce tem {idade} anos')

def pegarDados() -> None:

    for i in range(0, 3):
        nomes.append(input(f'Qual é o {i+1}º nome: '))
        idade.append(int(input(f'Qual a {i+1}ª idade: ')))

    for i in range(0, 3):
        inprimirDados(nomes[i], idade[i])

pegarDados()