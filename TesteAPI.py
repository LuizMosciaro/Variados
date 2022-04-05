from selenium.webdriver.common.by import By
from selenium import webdriver
from secret import api as a, login as l, senha as sn
from webdriver_manager.chrome import ChromeDriverManager
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.chrome.options import Options
import os


url = 'https://nfse-prd.manaus.am.gov.br/nfse/servlet/hlogin'
solver = TwoCaptcha(a)

def navegador():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s,options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="TABLE1"]/tbody/tr[6]/td/input')))
        driver.find_element(By.XPATH,'//*[@id="vUSULOGIN"]').send_keys(l)
        driver.find_element(By.XPATH,'//*[@id="vSENHA"]').send_keys(sn)
        
        #Aqui ele vai printar apenas o captcha, guardar no desktop e enviar para o 2captcha
        driver.find_element(By.XPATH,'//*[@id="Grid1ContainerRow_0001"]/td').screenshot(r'C:\Users\supor\Desktop\captcha.png')
        
        #Local onde salvar o print
        imagem = (r'C:\Users\supor\Desktop\captcha.png')
        
        #Pega a imagem e envia para o servidor 2captcha
        result = solver.normal(imagem) #'Result' trás 2 resultados: 'captchaId' e 'code', queremos apenas o 'code'
        print("Texto capturado:",result['code'])

        #Pega a variavel 
        driver.find_element(By.XPATH,'//*[@id="vVALORIMAGEM"]').send_keys(result['code'])
        #Botao de login
        driver.find_element(By.XPATH,'//*[@id="TABLE1"]/tbody/tr[6]/td/input').click()

        #Deleta a imagem depois de utilizada
        os.remove(imagem)

    except Exception as e:
        sys.exit(e)



if __name__=='__main__':
    navegador()



