import pyautogui as p
import tkinter
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


x = str(input("Informe a data de ontem no formato ddmmaa\n"))
i = 0
while i != 1:
    if len(x) != 6:
        print("Formato errado, certifique que não colocou barra ou ano em formato 'aaaa'")
        break
    else:
        login = "XXXX"
        senha = "XXXX"

        url = 'XXXXXXXXX.COM.BR'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="all"]/div[2]/form/div/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input')))
        #Escrevendo login/senha e entrando
        driver.find_element(By.XPATH,'//*[@id="all"]/div[2]/form/div/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys(login)
        driver.find_element(By.XPATH,'//*[@id="all"]/div[2]/form/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys(senha)
        driver.find_element(By.XPATH,'//*[@id="all"]/div[2]/form/div/div/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input').click()

        #Buscando o caminho para upload de arquivo
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="outrosCadastros_mais"]/div[2]')))
        driver.find_element(By.XPATH,'//*[@id="outrosCadastros_mais"]/div[2]').click()
        driver.find_element(By.XPATH,'//*[@id="outrosCadastrosBanco_mais"]').click()
        driver.find_element(By.XPATH,'//*[@id="outrosCadastrosBanco"]/a[1]').click()

        #Configurando o arquivo ret correto
        path =r'C:\Users\supor\Desktop\DB'

        for filename in os.listdir(path):
           with open(os.path.join(path, filename), 'r') as f:
               #Essa parte confirma o código(ag+contacorrente) db dentro do xml
               text = f.read()
               start = text.find('02RETORNO01COBRANCA') +26
               end = text.find('SUPERMERCADOS',start)
               substring = text[start:end].strip()
               codigo = '812800514802'


               #Captura se a data condiz com a data informada no inicio
               text1 = f.read()
               start1 = text.find('S.A.') +4
               end1 = text.find('01600BPI',start1)
               data = text[start1:end1]
               #substring3 = substring2[:2]+'/'+substring2[2:]
               #data_ajustada = substring3[:5]+'/'+substring3[5:]

               print("Data do arquivo ret:",data)

               #Começa o upload do arquivo
               if data == x:
                   print('Documento correto para upload\nIniciando processamento...')
                   y = path+f'\CN{x[:5]}B.ret'
                   #y = r'C:\Users\supor\Desktop\DB\CN21022B.ret'
                   driver.find_element(By.ID,'arquivo').send_keys(y)
                   driver.find_element(By.ID,'botao1').click()
                   #CONTINUAR DAQUI O CODIGO!!!!!
                   #_______________________________







               else:
                   print('ERRO: Confira a data utilizada ou se há mais de um arquivo na pasta')
                   driver.quit()
                   break
    i += 1


