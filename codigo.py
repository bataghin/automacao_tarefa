# Passo a passo do projeto

# 1 Abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#para instalar "pip install pyautogui"
import pyautogui
import time
pyautogui.PAUSE = 0.5

# pyautogui.click -  clicar com o mouse
# pyautogui.write - escreve texto
# pyautogui.press - pressiona uma tecla do teclado
# pyautogui.hotkey - apertar um conjunto de teclas (Ctrl C, Ctrl V)

# abrir o navegador 
time.sleep(2)
pyautogui.press("win")
time.sleep(2)
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)
# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# pode demorar mais p/ carregar o site
time.sleep(3)

# 2 Fazer login
pyautogui.click(x=464, y=412)
time.sleep(2)
pyautogui.write("testeaula@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("enter")
time.sleep(1)

# 3 Abrir/Importar a base de dados de produtos para cadastrar
#pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
# print(tabela)
time.sleep(2)

# 4 Cadastrar um produto

# para cada linha(index) dentro da minha tabela quero fazer todos os passos abaixo
for linha in tabela.index:
    #codigo = (tabela.loc[linha, coluna]
    cod = str(tabela.loc[linha, "codigo"])
    # clicar no campo do codigo do produto
    pyautogui.click(x=413, y=287)

    # preencher o codigo
    pyautogui.write(cod)
    # passar para o proximo campo
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar para o proximo campo
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar para o proximo campo
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar para o proximo campo
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar para o proximo campo
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    
    #obs
    obs = (str(tabela.loc[linha, "obs"]))
    #se obs for diferente de 'nan' vai fazer o preenchimento
    if obs != "nan":
        pyautogui.write(obs)
    # passar para o proximo campo
    pyautogui.press("tab")

    # apertar o botão
    pyautogui.press("enter")

    # arrastar a tela para cima
    pyautogui.scroll(5000)
    time.sleep(1)





# # 5 Repetir isso até acabar a lista de produtos

