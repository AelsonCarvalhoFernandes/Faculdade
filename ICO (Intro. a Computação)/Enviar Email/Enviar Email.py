import pyautogui as pd
import time
import pyperclip as pc
import os
#---------------Funções-----------------#
def clicar(x, y):
    pd.click(x, y)
    time.sleep(5)
def digitar(texto):
    pc.copy(texto)
    pd.hotkey('ctrl', 'v')
    pd.hotkey('enter')
    time.sleep(5)
def abrirsoftware(software):
    os.startfile(software)
    time.sleep(5)
def tab():
    pd.hotkey('tab')
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
clicar(x=85, y=178)
clicar(x=940, y=316)
digitar("") # Destinatário
tab()
digitar('Teste') # Titulo
tab()
digitar('Mensagem de teste da atividade de enviar email em python') # Mensagem
clicar(x=957, y=694)
clicar(x=327, y=46)
digitar("D:\Meus Arquivos\Documents\Projetos\Faculdade\ICO\Enviar email") # Localização do arquivo tipo C:\ Documentos\ Artuivo.txt
clicar(x=275, y=165)
clicar(x=514, y=445)
clicar(x=840, y=688)