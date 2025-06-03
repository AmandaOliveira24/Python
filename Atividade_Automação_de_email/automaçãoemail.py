import pyautogui
import time

pyautogui.press('win')
time.sleep(2)
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=886, y=46)
time.sleep(2)
pyautogui.write('www.gmail.com')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=1106, y=570)
time.sleep(4)
pyautogui.write('amanda.sou18@gmail.com')
pyautogui.press('enter')
