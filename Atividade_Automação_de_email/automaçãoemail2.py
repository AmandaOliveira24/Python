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

def escreva_algo(nome, delay = 2):
    espera(delay)
    pyautogui.write(nome)
    espera(delay)
    pyautogui.press('enter')
    espera(1)


pyautogui.press('win')
espera()
pyautogui.press('enter')
escreva_algo('www.gmail.com')

clique(1145,532)
espera()
escreva_algo('amanda.sousoliv18@gmail.com')
espera()
escreva_algo('-')
clique(76,175)
escreva_algo('mateus@to.senac.br')
clique(1329,518)
escreva_algo('olha fessor eu consegui!')
clique(1311,998)
clique(1419,999)
clique(83,266)
clique(815,58)
escreva_algo('olha fessor eu consegui!')













