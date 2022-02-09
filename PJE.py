import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#x = str(input("Qual número do processo?"))
num_processo = '0010101-34.2017.5.15.0010'

url = 'https://pje.trt15.jus.br/consultaprocessual/'
driver = webdriver.Chrome()
driver.get(url)

#Pegando o número do processo e entrando na pagina (1Grau apenas)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="brasao"]')))
driver.find_element(By.XPATH,'//*[@id="nrProcessoInput"]').send_keys(num_processo)
driver.find_element(By.XPATH,'//*[@id="btnPesquisar"]').send_keys(Keys.ENTER)
#Clicando no botao do 1Grau
WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="painel-escolha-processo"]/button[1]')))
driver.find_element(By.XPATH,'//*[@id="painel-escolha-processo"]/button[1]').click()
#Escrevendo a Captcha, tem 6segundos para escrever
time.sleep(6)
driver.find_element(By.XPATH,'//*[@id="btnEnviar"]').click()
#Clicando no cabeçalho para recolher infos importantes:
WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="titulo-detalhes"]/h1')))
driver.find_element(By.XPATH,'//*[@id="titulo-detalhes"]/h1').click()
#Coletando as infos:
orgao = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dd[1]').text
distribuido = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dd[2]').text
autuado = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dd[3]').text
valor = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dd[4]').text
lista = []
lista.append(orgao)
lista.append(distribuido)
lista.append(autuado)
lista.append(valor[3:])
coluna = [1,2,3,4]
dicion = dict(zip(lista,coluna))

df = pd.DataFrame(coluna,columns=['orgao','distribuido','autuado','valor'])
print(df)