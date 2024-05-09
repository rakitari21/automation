
import pyautogui

import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar alguima tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de de teclas (Crtl C, Crtl V, Alt Tab)
 

pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("Enter")


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")

time.sleep(2) 


pyautogui.click(x=547, y=353)
pyautogui.write("chupacabra@hotmail.com")


pyautogui.press("Tab")


pyautogui.write("Andre0227")


pyautogui.click(x=757, y=515)



import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    
    pyautogui.click(x=469, y=241)

    
    pyautogui.write(codigo)
    pyautogui.press("Tab")
    
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("Tab")
    
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("Tab")

    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    
    pyautogui.press("Tab")

    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    
    pyautogui.press("Tab")
    

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("Tab")
    
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("Tab")

    
    pyautogui.press("enter")
    pyautogui.scroll(5000)