'''
4. Um estacionamento cobra R$5,00 por um período de até 3h. Para cada hora adicional,
ele cobra R$1,50. As horas são sempre contadas como inteiros. Escreva um algoritmo
e um DFD que receba como entrada a hora que o cliente entrou com o carro e a hora
que o cliente saiu (em minutos e segundos), considerando apenas quantidades inteiras
de horas de forma que cada minuto a mais configura uma nova hora.
Obs.: A hora será sempre informada em intervalos de 24h, não havendo, por exemplo,
3 horas da tarde, mas 15 horas e o carro sempre sairá no mesmo dia em que entrou.
Ex:
Horário de Entrada: 10h e 20min
Horário de Saída: 13h e 20min
Total a pagar: R$ 5,00
Horário de Entrada: 10h e 20min
Horário de Saída: 13h e 21min
Total a pagar: R$ 6,50 : R$ 5,00 + R$ 1,50
'''
import math

horaent = float(input('Digite o horário de entrada do veiculo:'))
minutent = float(input('Digite os minutos de entrada:'))
horasai = float(input('Digite a hora de saida em horas:'))
minutsai = float(input('Digite os minutos da saida:'))


totalhoras= (horasai + (minutsai/100 ))-(horaent +(minutent/100))

valor3horas = 5
valorHoraadi = 1.50

print(totalhoras)

if totalhoras <= 3:
    print(f'O valor a pagar é R${valor3horas:.2f}')
elif totalhoras > 3:
    horas = totalhoras
    horasextras = horas - 3
    if horasextras > 0:
        totalhorasext= math.ceil(horasextras)
        valorapagar = valor3horas + (totalhorasext*valorHoraadi)
        print(f'O valor a ser pago é R${valorapagar:.2f}')
    
