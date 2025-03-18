import pyautogui
from time import sleep
#Login
pyautogui.click(954,540, duration=0.5)
pyautogui.write('admin')
pyautogui.click(952,572, duration=0.52)
pyautogui.write('admin')
pyautogui.click(872,597, duration=0.5)

#abrir arquivo
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]                        
        preco = linha.split(',')[2]
        #Cadastrar produtos
        pyautogui.click(677,528, duration=0.5)
        pyautogui.write(produto)
        pyautogui.click(684,551, duration=0.5)
        pyautogui.write(quantidade)
        pyautogui.click(683,579, duration=0.5)
        pyautogui.write(preco)
        pyautogui.click(599,740, duration=0.5)
        sleep(1)