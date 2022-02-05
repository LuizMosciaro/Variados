from bs4 import BeautifulSoup
import requests
from random import randint
import time
import pandas as pd
import pywhatkit as pw
import pyautogui as py

lista_textos = []
lista_autores = []
index = 0

for num_de_pagina in range(1, 10):                           #loop para pegar varias paginas, o segundo numero define o numero de paginas a procurar
    url = 'https://www.pensador.com/frases_de_motivacao/'
    page = requests.get(url + str(num_de_pagina) + '/')     #a pagina vai ser a url + o numero de pagina do in range
    soup = BeautifulSoup(page.content, 'html.parser')       #faz a soup + parser
    frase = soup.findAll('p', attrs={'class': 'frase fr'})  #encontra o elemento desejado (frase nesse caso)
    autor = soup.findAll('span', attrs={'class': 'autor'})  #encontra o elemento desejado (autor)
    randomizador = randint(2, 4)                            #randomiza a soneca para não bloquear meu ip e dorme
    time.sleep(randomizador)
    print("______________________________________")
    print(f"Dormiu por {randomizador} segundos")            #informa no console
    print(f"Buscando em página {num_de_pagina}", end=" ")   #mostra a busca no console
    print(".",end="")
    time.sleep(0.5)
    print(" ",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print(" ",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print(" ",end="")
    time.sleep(0.5)
    print(".")
    print("______________________________________")
    for x, y in zip(frase, autor):                          #pega os 2 elementos e une em um 'zip'
        frase_txt = str(x.text)                             #transforma para string
        autor_txt = str(y.text[1:])                         #transforma para string A PARTIR dos indice 1 (pois tem um \n) na frente do nome autor
        lista_textos.append(frase_txt)                      #coloca a string na lista global
        lista_autores.append(autor_txt)

df = pd.DataFrame({'':lista_textos,' ':lista_autores})              #ATENÇÃO AO FORMATO: ({}) SE FALTA ALGUM DESSES DA ERRO!!!
pd.set_option('display.max_colwidth', 999)                          #faz alongar o texto que aparece, se não fica cortado se enviar para o whatsapp (no excel fica completo)
df[' '] = '('+df[' '].astype(str)+')'                               #colocando "()" entre a coluna do autor
df[''] = '"'+df[''].astype(str)+'"'


print(f"Foram encontrados {len(lista_textos)} frases em {num_de_pagina} páginas")
print("Iniciando envio de mensagens via Whatsapp...")

for i in range(1,2):
    whatsapp = "+5592992534185"
    amostra = df.sample().to_string(index=False)              #to_string(index=False) tira  o numerozinho do indice da linha
    pw.sendwhatmsg_instantly(f"{whatsapp}", f"{amostra}", 15, tab_close=True,close_time=4)
    py.click(1327, 705)
    time.sleep(3)
    py.click(1327, 705)
    time.sleep(3)
    print(f'A {str(i)} frase enviada foi:',amostra)



print("\nFechando o script...")





