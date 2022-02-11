from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as c
from openpyxl import load_workbook
import pyautogui as p

index = 2
# Abrindo excel
file = r'C:\Users\supor\Desktop\PXTeste.xlsx'
wb = load_workbook(file)
ws = wb.active

# TODA A CONSULTA ABAIXO FUNCIONA APENAS PARA O PRIMEIRO GRAU DO PROCESSO
# ________________________________________________________________________

for i in range(1, len(ws['A'])):  # é o loop, que irá de 1 até ''len(ws['A'])''<- Pega a coluna A do worksheet do excel, calcula quantos itens tem e diz que é o tamanho do range do loop for
    # Inicializando o chrome maximizado
    url = 'https://pje.trt15.jus.br/consultaprocessual/'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    # Pegando os processos
    num_processo = ws.cell(row=index, column=1).value
    print("\nRealizando a consulta no processo: " + str(num_processo))

    # Pegando o número do processo e entrando na pagina
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'label-sistema')))
    driver.find_element(By.XPATH, '//*[@id="nrProcessoInput"]').send_keys(num_processo)
    driver.find_element(By.XPATH, '//*[@id="btnPesquisar"]').send_keys(Keys.ENTER)

    # Clicando no botao do 1Grau
    sleep(2)
    p.moveTo(667, 357)
    p.click()

    # Clicando no campo de escrever a captcha
    sleep(2)
    p.moveTo(650, 446)
    p.click()

    # Escrevendo a Captcha, tem 6segundos para escrever
    sleep(8)
    driver.find_element(By.XPATH, '//*[@id="btnEnviar"]').click()

    # Essa condição verifica se há a palavra 'sentença', se houver pula pro proximo
    sleep(3)
    x = driver.find_element(By.XPATH, '//*[@id="cabecalhoVisualizador"]/mat-card-title').text[13:]
    if x == 'Sentença':
        print(f"Processo {num_processo} há sentença")
        print(f'Consulta {index - 1} finalizada..')
        sentencatxt = "OBS: Tem sentença proferida"
        ws.cell(column=2, row=index, value=sentencatxt)
        index += 1
        continue

    # Coletando Juiz: // A coleta do juiz começa aqui pq é antes do click no cabeçalho
    sleep(2)
    juiz = driver.find_element(By.XPATH, '//*[@id="cabecalhoVisualizador"]/mat-card-subtitle').text
    j = str(juiz)
    inicio = j.find("por") + 3
    final = j.find("em", inicio)
    substrg = j[inicio:final]
    c.copy(substrg)
    text = c.paste()
    ws.cell(column=11, row=index, value=text)

    # Clicando no cabeçalho para recolher infos importantes:
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="titulo-detalhes"]/h1')))
    driver.find_element(By.XPATH, '//*[@id="titulo-detalhes"]/h1').click()

    # Coletando Orgão:
    orgao = driver.find_element(By.XPATH, '//*[@id="colunas-dados-processo"]/div[1]/dl/dd[1]').text
    c.copy(orgao)
    text = c.paste()
    ws.cell(column=2, row=index, value=text)

    # Coletando Distribuido:
    distribuido = driver.find_element(By.XPATH, '//*[@id="colunas-dados-processo"]/div[1]/dl/dd[2]').text
    c.copy(distribuido)
    text = c.paste()
    ws.cell(column=3, row=index, value=text)

    # Coletando Autuado:
    autuado = driver.find_element(By.XPATH, '//*[@id="colunas-dados-processo"]/div[1]/dl/dd[3]').text
    c.copy(autuado)
    text = c.paste()
    ws.cell(column=4, row=index, value=text)

    # Coletando Valor:
    valor = driver.find_element(By.XPATH, '//*[@id="colunas-dados-processo"]/div[1]/dl/dd[4]').text
    c.copy(valor)
    text = c.paste()
    ws.cell(column=5, row=index, value=text)

    # Coletando Justica:
    justica = driver.find_element(By.XPATH, '//*[@id="colunas-dados-processo"]/div[1]/dl/dt[5]').text
    c.copy(justica)
    text = c.paste()
    ws.cell(column=6, row=index, value=text)

    # Coletando Polo Ativo:
    p.tripleClick(x=558, y=302)
    p.hotkey('ctrl', 'c')
    text = c.paste()
    ws.cell(column=7, row=index, value=text)

    # Coletando Polo Ativo ADVOGADO:
    p.tripleClick(x=683, y=327)
    p.hotkey('ctrl', 'c')
    text = c.paste()
    ws.cell(column=8, row=index, value=text)

    # Coletando Polo Passivo:
    p.tripleClick(x=898, y=301)
    p.hotkey('ctrl', 'c')
    text = c.paste()
    ws.cell(column=9, row=index, value=text)

    # Coletando Polo Passivo ADVOGADO:
    p.tripleClick(x=963, y=327)
    p.hotkey('ctrl', 'c')
    text = c.paste()
    ws.cell(column=10, row=index, value=text)

    # Coletando Assuntos:
    sleep(2)
    orgao = driver.find_element(By.XPATH, '//*[@id="colunas-dados-processo"]/div[1]').text + '...'
    x = str(orgao)  # Garantindo que ta em formato de string
    inicio = x.find(
        "Assunto(s):") + 11  # Encontrando o elemento "Assuntos" e definindo que será o inicio da substring, adicionar +11 exclui o elemento (Assunto(s) tem 11 chars)
    final = x.find("...",
                   inicio)  # Note que na linha 123 adicionei reticencias para delimitar como sendo o final da string orgao
    substring = x[inicio:final]  # Criando a substring, que vem da 'x' a partir do inicio até o final
    c.copy(substring)  # Copiando a substring para o clipboard
    assuntos2 = c.paste()
    ws.cell(column=12, row=index, value=assuntos2)  # Inserindo na planilha

    # Salvando a planilha com os dados
    wb.save(file)
    print(f'Consulta {index - 1} finalizada..')
    # Add +1 a variavel global index, para que ela seja '2' no proximo loop
    index += 1


print("\nPrograma finalizado")



