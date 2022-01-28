import time
import pyautogui

#Para descobrir a posição do mouse constantemente pelo cmd do windows:
#Cmd>python>import pyautogui>pyautogi.displayMousePosition()

py = pyautogui

print('Abrindo o Chrome')

py.hotkey('winleft','r')        #hotkey = atallho
py.write('chrome.exe')          #escreve o executavel do chrome
time.sleep(1.5)
py.press('enter')

time.sleep(20)


print('Abrindo o Hiveos')

py.write('https://the.hiveos.farm/')
py.press('enter')

time.sleep(12)                   #dorme

py.click(x=160,y=445)           #leva o mouse para a coordenada solicitada

time.sleep(8)

py.click(x=155,y=445)

time.sleep(2)

py.hotkey('ctrl','t')           #abre uma nova janela, atraves do atalho crtl+t do chrome
print('Abrindo o Youtube')
py.write('https://www.youtube.com/')
py.press('enter')





