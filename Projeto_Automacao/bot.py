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
for linha in range(0,1):
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    observacao = tabela.loc[linha, "obs"]
    pyautogui.write(str(observacao))

    pyautogui.press("enter")

