import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# pyautogui.scroll -> rola a tela - negativo vai para baixo, positivo vai para cima

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.press("tab")

pyautogui.press("tab")

pyautogui.press("enter")

link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

time.sleep(3)

pyautogui.press("tab")

email="teste@gmail.com"
pyautogui.write(email)

pyautogui.press("tab")

senha="senhadificilprakrl"
pyautogui.write(senha)

pyautogui.press("enter")

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:

    pyautogui.press("tab")
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))

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
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.click(x=50, y=300)
    