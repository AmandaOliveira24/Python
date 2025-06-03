import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import sys 

webbrowser.open('https://web.whatsapp.com/')
sleep(10)
workbook = openpyxl.load_workbook('aprovacao.xlsx')
pagina_cliente = workbook['Plan1']
for linha in pagina_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    situacao = linha[2].value

    if nome is None or telefone is None:
        break

    mensagem = f'Olá {nome} você foi {situacao} na nossa UC de Programação de sistemas para desktop
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

    webbrowser.open(link_mensagem_whatsapp)

    sleep(10)
    pyautogui.click(x=1713, y=978)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    sleep(5)
sys.exit()  


















