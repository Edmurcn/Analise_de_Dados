import pyautogui
import time
import pandas as pd 

pyautogui.PAUSE = 0.5

#entrar no navegador
pyautogui.hotkey("win", "tab")
time.sleep(1)

for i in range(1, 80):
    #selecionar mensagem
    pyautogui.click(x=417, y=220)
    time.sleep(1)

    #apagar
    pyautogui.click(x=564, y=220)
    time.sleep(2)

print("Ok!")    
