# bibliotecas -> pip install pyautogui
# pip install pandas openpyxl # para trabalhar com excel e planilhas

import pyautogui
import time
import pandas

# pyautogui.click -- click do mouse
# pyautogui.write -- escreve um texto
# pyautogui.press -- aperta o enter
# pyautogui.hotkey -- aperta um atalho

pyautogui.PAUSE = 0.5 # Espera para executar os comandos

url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Comandos para abrir o navegador:
pyautogui.press("win") #tecla windows
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1353, y=101)
pyautogui.write(url)
pyautogui.press("enter")
time.sleep(5)

# Preenchendo os campos Email e Senha:
pyautogui.click(x=585, y=560)
pyautogui.write("test@test.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Abrir a base de dados no csv:

tabela = pandas.read_csv("PYTHON POWERUP\produtos.csv")
print(tabela)

# Repetir o processo de cadastro abaixo para a lista do csv
for linha in tabela.index:
    # Cadastrar produto:
    pyautogui.click(x=682, y=301)
    #codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # #preco_unitario
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    #custo#
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    
    pyautogui.scroll(5000) #volta para o início da tela








