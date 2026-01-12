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
pyautogui.write(url)
pyautogui.press("enter")
time.sleep(3)

# Preenchendo os campos Email e Senha:
pyautogui.click(x=674, y=447)
pyautogui.write("test@test.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Abrir a base de dados no csv:

tabela = pandas.read_csv("produtos.csv")
print(tabela)


