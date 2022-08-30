from tkinter import *
from tkinter import messagebox

# Funções ----------------------------------------------------------------------------------------------------------------------------------------------
def DecimalBinario():
    try:
        conversao = int(n1.get())
        binario = bin(conversao) # Converte o valor em decimal
        binario = str(binario) # Converte o valor em string para poder tratar do valor
        binario = binario.replace(binario[0], "", 1) # Como a conversão gera 2 valores no inicio que não faz parte do resultado então removi com esse replace
        valor_final = binario.replace(binario[0], "", 1) # Como a conversão gera 2 valores no inicio que não faz parte do resultado então removi com esse replace
        return res_txt.set(valor_final + " Binario") # Envia o valor para a interface
    except:
        messagebox.showinfo("Ajuda", "Este botão converte de Decimal para Binário. Por favor corrigir o número")

def BinarioDecimal():
    try:
        conversao = int(n1.get(), 2) # Converte binário em inteiro
        return res_txt.set(f"{conversao} Decimal") # Envia o valor para a interface
    except:
        messagebox.showinfo("Ajuda", "Este botão converte de Binario para Decimal. Por favor corrigir o número")

def DecimalOctal():
    try:
        conversao = int(n1.get())
        octal = oct(conversao) # Converte o valor em Octal
        octal = str(octal) # Converte o valor em string para poder tratar do valor
        octal = octal.replace(octal[0], "", 1) # Como a conversão gera 2 valores no inicio que não faz parte do resultado então removi com esse replace
        valor_final = octal.replace(octal[0], "", 1) # Como a conversão gera 2 valores no inicio que não faz parte do resultado então removi com esse replace
        return res_txt.set(valor_final + " Octal") # Envia o valor para a interface
    except:
        messagebox.showinfo("Ajuda", "Este botão converte de Decimal para Octal. Por favor corrigir o número")

def OctalDecimal():
    try:
        conversao = int(n1.get(), 8) # Converte octal para inteiro
        return res_txt.set(conversao + " Decimal") # Envia o valor para a interface
    except:
        messagebox.showinfo("Ajuda", "Este botão converte de Octal para Decimal. Por favor corrigir o número")

def DecimalHexadecimal():
    try:
        conversao = int(n1.get())
        hexa = hex(conversao) # Converte o valor em hexadecimal
        hexa = str(hexa) # Converte o valor em string para poder tratar do valor
        hexa = hexa.replace(hexa[0], "", 1) # Como a conversão gera 2 valores no inicio que não faz parte do resultado então removi com esse replace
        valor_final = hexa.replace(hexa[0], "", 1) # Como a conversão gera 2 valores no inicio que não faz parte do resultado então removi com esse replace
        return res_txt.set(valor_final + " Hexadecimal") # Envia o valor para a interface
    except:
        messagebox.showinfo("Ajuda", "Este botão converte de Decimal para Hexadecimal. Por favor corrigir o número")

def HexadecimalDecimal():
    try:
        conversao = int(n1.get(), 16) # Converte hexadecimal em inteiro
        return res_txt.set(f"{conversao} Decimal") # Envia o valor para a interface
    except:
        messagebox.showinfo("Ajuda", "Este botão converte de Hexadecimal para Decimal. Por favor corrigir o número")

# ------------------------------------------------------------------------------------------------------------------------------------------------------
calculadora = Tk()
# Configuração da janela -------------------------------------------------------------------------------------------------------------------------------
calculadora.title("Calculadora")
calculadora.geometry("400x210")
calculadora.resizable(0, 0)
calculadora.configure(background="#4F4F4F")
calculadora.iconbitmap("346399.ico")


#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Conteudo da janela -----------------------------------------------------------------------------------------------------------------------------------
f1 = Frame(calculadora, relief="raised", borderwidth=1, background="#A9A9A9").place(x=10, y=10, width=380, height=50)

n1 = Entry(f1, font="Arial 20", relief="sunken")
n1.place(x=30, y=15, width=335, height=35)

res_txt = StringVar(calculadora)

f2 = Frame(calculadora, relief="raised", borderwidth=1, background="#A9A9A9").place(x=10, y=70, width=380, height=80)

decimalbinario = Button(f2 ,text='Decimal>Binário', command=lambda: DecimalBinario())
decimalbinario.place(x=30, y=75)

binariodecimal = Button(f2, text="Binario>Decimal", command=lambda: BinarioDecimal())
binariodecimal.place(x=30, y=110)

decimaloctal = Button(f2, text="Decimal>Octal", command=lambda: DecimalOctal())
decimaloctal.place(x=140, y=75)

octaldecimal = Button(f2, text="Octal>Decimal", command=lambda: OctalDecimal())
octaldecimal.place(x=140, y=110)

decimalhexadecimal = Button(f2, text="Decimal>Hexadecimal", command=lambda: DecimalHexadecimal())
decimalhexadecimal.place(x=240, y=75)

hexadecimaldecimal = Button(f2, text="Hexadecimal>Decimal", command=lambda: HexadecimalDecimal())
hexadecimaldecimal.place(x=240, y=110)


f3 = Frame(calculadora, relief="raised", borderwidth=1, background="#A9A9A9").place(x=10, y=160, width=380, height=40)
Label(calculadora, text="Resultado:", font="Arial 14", background="#A9A9A9").place(x=20, y=165)
res =Label(calculadora, textvariable=res_txt, relief="solid", borderwidth=1, font="Arial 12").place(x=120, y=165, width=250, height=30)

# -------------------------------------------------------------------------------------------------------------------------------------------------------
calculadora.mainloop()