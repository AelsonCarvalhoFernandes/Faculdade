'''
1. Em uma loja, compras a prazo possuem juros simples de 2% ao mês. Já as compras a
vista, possuem desconto de 10%. Escreva um algoritmo e um DFD que leia do
usuário o valor da compra, e a forma de pagamento (1: pagamento a vista – 2:
pagamento a prazo) o prazo, no caso das compras a prazo, e informe total a pagar ou o
valor da parcela mensal da mercadoria.
Ex: Uma mercadoria que custe R$100,00 e será parcelada em 5 vezes, terá um
acréscimo de 10% e, portanto valor total de R$110,00, sendo dividido em 5 parcelas
de $22,00.
Esta mesma mercadoria à vista teria um total a pagar de R$90,00
'''
p_juros = 0.02
p_desconto = 0.10

tipo_de_compra = int(input('Digite a forma de pagamento: [1] A vista, [2] Parcelado\n'))

valor_mercadoria = int(input('Digite o valor da mercadoria: R$\n'))

if tipo_de_compra == 2:
    quant_parcelas = int(input('Quantidade de parcelas:\n'))
    
    valor_acrescimo = valor_mercadoria*p_juros

    valor_parcelas = (valor_mercadoria/quant_parcelas)+valor_acrescimo

    print(f'O valor das {quant_parcelas} parcelas é R${valor_parcelas:.2f}')

elif tipo_de_compra == 1:
    valor_desconto = valor_mercadoria*p_desconto

    valor_total = valor_mercadoria - valor_desconto

    print(f"O valor total a pagar é R${valor_total:.2f}")

