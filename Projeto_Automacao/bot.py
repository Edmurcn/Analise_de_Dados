import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

#entrar no navegador
pyautogui.press("win")
time.sleep(1)

pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")

#entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')
time.sleep(2)

#cadastro
pyautogui.press("tab")
pyautogui.write("edmurcn@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("enter")
pyautogui.press("tab")

#cadastro do produto

tabela = pd.read_csv("/home/edmurcn/Documentos/MeusProjetos/Analise_de_Dados/Projeto_Automacao/produtos.csv")

linha = 0
for linha in tabela.index:

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(500)
    pyautogui.click(x = 966, y = 285)





