import pyautogui as pd
import time
import pyperclip as pc
import os
#---------------Funções-----------------#
def printscreen():
    pd.hotkey('WIN', 'prtscr')
def clicar(x, y):
    pd.click(x, y)
    time.sleep(1)
def digitar(texto):
    pc.copy(texto)
    pd.hotkey('ctrl', 'v')
    pd.hotkey('enter')
    time.sleep(5)
def apenasdigitar(texto):
    pc.copy(texto)
    pd.hotkey('ctrl', 'v')
    time.sleep(2)
def abrirsoftware(software):
    os.startfile(software)
    time.sleep(5)
def tab():
    pd.hotkey('tab')
#----------- Pesquisa Passagens ----------#
abrirsoftware("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") # O navegador microsoft edge
clicar(x=1335, y=43)
clicar(x=1202, y=148)
clicar(x=496, y=54)
digitar("https://123milhas.com/?msclkid=e560c726dfc6195a7bb3a58b11b7eda7&utm_source=bing&utm_medium=cpc&utm_campaign=BING%20-%2001%20Palavras%20Novas%20-%20Desktop&utm_term=passagens%20a%C3%A9reas&utm_content=G6%20-%20Termos")
clicar(x=184, y=367)
apenasdigitar("Porto Seguro")
clicar(x=173, y=432)
clicar(x=419, y=374)
apenasdigitar("São Paulo")
clicar(x=441, y=438)
clicar(x=665, y=371)
clicar(x=665, y=371)
clicar(x=665, y=371)
apenasdigitar("10/08/2022")
clicar(x=762, y=375)
clicar(x=762, y=375)
clicar(x=762, y=375)
apenasdigitar("20/08/2022")
clicar(x=1289, y=162)
clicar(x=1155, y=374)
clicar(x=1155, y=374)
clicar(x=1155, y=374)
pd.sleep(30)
printscreen()
clicar(x=1347, y=7)
clicar(x=1347, y=7)


#-----------Enviar E-mail-------------#
abrirsoftware("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") # O navegador microsoft edge
clicar(x=1335, y=43)
clicar(x=1202, y=148)
clicar(x=496, y=54)
digitar("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
clicar(x=601, y=362)
digitar("") # E-mail de login
clicar(x=800, y=553)
clicar(x=611, y=383)
digitar("") # Senha
clicar(x=818, y=501)
clicar(x=25, y=179)
clicar(x=940, y=316)
digitar("") # Destinatário
tab()
digitar('Teste') # Titulo
tab()
digitar('Mensagem de teste da atividade de enviar email em python. nesse caso é o de passagens de Porto seguro a São paulo') # Mensagem
clicar(x=957, y=694)
clicar(x=327, y=46)
digitar("D:\Meus Arquivos\Pictures\Screenshots") # Localização do arquivo tipo C:\ Documentos\ Artuivo.txt
clicar(x=214, y=155)
clicar(x=514, y=445)
clicar(x=840, y=688)
#----------------------------------------------------#