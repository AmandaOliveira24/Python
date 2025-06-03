import pyautogui
import time

def espera(segundos =2):
    time.sleep(segundos)

def clique(x, y, delay = 2):
    espera(delay)
    pyautogui.click(x = x, y = y)

def dois_cliques(x, y, delay = 2):
    espera(delay)
    pyautogui.doubleClick(x = x, y = y)

def abrir_site(nome_site, delay = 2):
    espera(delay)
    pyautogui.write(nome_site)
    espera(delay)
    pyautogui.press('enter')
    espera(1)

# pyautogui.click(x=1792, y=7)
# pyautogui.doubleClick(x=22, y=136)

clique(1792,7)
dois_cliques(22,136)
abrir_site('https://www.to.senac.br/')
clique(884,26)
clique(1182,261)
clique(1218,435)

























