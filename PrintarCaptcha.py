import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as p

x = 389
y = 312
width = 676 - x
height = 377 - y
for i in range(1,11):
    url = 'https://pje.trt4.jus.br/consultaprocessual/captcha/detalhe-processo/0021160-41.2015.5.04.0383/1'
    path = r'C:\Users\supor\PycharmProjects\pythonProject\screenshots'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    printscreen = p.screenshot(region=(x,y,width,height))
    printscreen.save(path+rf"\{i}.png")
    driver.quit()
