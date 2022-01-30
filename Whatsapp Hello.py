import time
import pywhatkit as k
import pyautogui as p

for i in range(1,4):
    k.sendwhatmsg_instantly("+5592992534185",
                   "*Esta é uma mensagem automatica via Python Pywhatkit..*",
                    10,False)
    p.click(1327,705)
    time.sleep(12)
