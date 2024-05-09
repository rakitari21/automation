# Passo a passo do projeto

# 1. Abrir o sistema
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar biblioteca: pip install pyautogui
import pyautogui

import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar alguima tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de de teclas (Crtl C, Crtl V, Alt Tab)
 
# abrir navegador (Opera)
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("Enter")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")

time.sleep(2) 

# 2. Fazer login

pyautogui.click(x=547, y=353)
pyautogui.write("chupacabra@hotmail.com")


pyautogui.press("Tab")


pyautogui.write("Andre0227")


pyautogui.click(x=757, y=515)




# 3. Importar base de dados 

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


# 4. Cadastrar produtos

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do produto
    pyautogui.click(x=469, y=241)

    #preencher o codigo
    pyautogui.write(codigo)
    #passar para o proximo campo
    pyautogui.press("Tab")

    # marca
    #preencher o codigo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    #passar para o proximo campo
    pyautogui.press("Tab")

    #tipo
    #preencher o codigo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    #passar para o proximo campo
    pyautogui.press("Tab")

    #categoria
    #preencher o codigo
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    #passar para o proximo campo
    pyautogui.press("Tab")

    #preco
    #preencher o codigo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    #passar para o proximo campo
    pyautogui.press("Tab")

    #custo
    #preencher o codigo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    #passar para o proximo campo
    pyautogui.press("Tab")

    #OBS
    #preencher o codigo
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    #passar para o proximo campo
    pyautogui.press("Tab")


    # clicar em enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# 5. Repetir o processo

