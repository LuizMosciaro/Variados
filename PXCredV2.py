from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as c
from openpyxl import load_workbook
import pyautogui as p

index = 1
# Abrindo excel
file = r'C:\Users\supor\Desktop\PXTeste.xlsx'
wb = load_workbook(file)
ws = wb.active

for i in range(1,2):

    # Inicializando o chrome maximizado
    url = 'https://pje.trt15.jus.br/consultaprocessual/'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    #Pegando os processos
    num_processo = ws.cell(row=index + 1, column=1).value

    #Pegando o número do processo e entrando na pagina (1Grau apenas)
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'label-sistema')))
    driver.find_element(By.XPATH,'//*[@id="nrProcessoInput"]').send_keys(num_processo)
    driver.find_element(By.XPATH,'//*[@id="btnPesquisar"]').send_keys(Keys.ENTER)

    #Clicando no botao do 1Grau
    sleep(2)
    p.moveTo(667,357)
    p.click()

    #Clicando no campo de escrever a captcha
    sleep(2)
    p.moveTo(650, 446)
    p.click()

    #Escrevendo a Captcha, tem 6segundos para escrever
    sleep(8)
    driver.find_element(By.XPATH,'//*[@id="btnEnviar"]').click()

    #Clicando no cabeçalho para recolher infos importantes:
    WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="titulo-detalhes"]/h1')))
    driver.find_element(By.XPATH,'//*[@id="titulo-detalhes"]/h1').click()

    #Coletando Orgão:
    orgao = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dd[1]').text
    c.copy(orgao)
    text = c.paste()
    ws.cell(column=2, row=index + 1, value=text)

    #Coletando Autuado:
    autuado = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dd[3]').text
    c.copy(autuado)
    text = c.paste()
    ws.cell(column=3, row=index + 1, value=text)

    #Coletando Valor:
    valor = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dd[4]').text
    c.copy(valor)
    text = c.paste()
    ws.cell(column=4, row=index + 1, value=text)

    #Coletando Justica:
    justica = driver.find_element(By.XPATH,'//*[@id="colunas-dados-processo"]/div[1]/dl/dt[5]').text
    c.copy(justica)
    text = c.paste()
    ws.cell(column=5, row=index + 1, value=text)

    #Coletando Polo Ativo:
    p.tripleClick(x=558,y=302)
    p.hotkey('ctrl','c')
    text = c.paste()
    ws.cell(column=6, row=index + 1, value=text)

    #Coletando Polo Ativo ADVOGADO:
    p.tripleClick(x=683,y=327)
    p.hotkey('ctrl','c')
    text = c.paste()
    ws.cell(column=7, row=index + 1, value=text)

    #Coletando Polo Passivo:
    p.tripleClick(x=898,y=301)
    p.hotkey('ctrl','c')
    text = c.paste()
    ws.cell(column=8, row=index + 1, value=text)

    #Coletando Polo Passivo ADVOGADO:
    p.tripleClick(x=963,y=327)
    p.hotkey('ctrl','c')
    text = c.paste()
    ws.cell(column=9, row=index + 1, value=text)

    #Salvando a planilha com os dados
    wb.save(file)

    #Add +1 a variavel global index, para que ela seja '2' no proximo loop
    index += 1


