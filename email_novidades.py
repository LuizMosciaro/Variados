import smtplib, ssl
import requests


cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
resjson = cotacao.json()
cotacao_string = str('Dolar/Real hoje: '+str(resjson['USDBRL']['bid'])[:4]+' $BRL'+'\nBitcoin/Real hoje: '+str(resjson['BTCBRL']['bid'])+' $BRL')

conselhos = requests.get('https://api.adviceslip.com/advice')
randomj = conselhos.json()
string_conselho = "Conselho do dia: "+str(randomj['slip']['advice'])


url2 = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring2 = {"q":"-3.0734136,-60.0094607"}

headers2 = {
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
	"X-RapidAPI-Key": "b0138569camsh41376bdd85486c3p1a0affjsn2621aff47a9a"
}

temperature = requests.request("GET", url2, headers=headers2, params=querystring2)
respjson2 = temperature.json()
temperatura = str('Em Manaus, a temperatura é: '+str(respjson2['current']['temp_c'])+'C, com sensação de: '+str(respjson2['current']['feelslike_c'])+'C')


url3 = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

querystring3 = {"sign":"Scorpio","day":"today"}

headers3 = {
	"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "b0138569camsh41376bdd85486c3p1a0affjsn2621aff47a9a"
}

signo = requests.request("POST", url3, headers=headers3, params=querystring3)
respon3 = signo.json()
signo_texto = str(respon3['description'])


url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

querystring = {"langpair":"en|pt","q":f"{string_conselho}","mt":"1","onlyprivate":"0"}

headers = {
	"X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com",
	"X-RapidAPI-Key": "b0138569camsh41376bdd85486c3p1a0affjsn2621aff47a9a"
}

tradutor = requests.request("GET", url, headers=headers, params=querystring)
respjson = tradutor.json()
tradutor_string = str(respjson['responseData']['translatedText'])


port = 465  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "seu@email.com"
receiver_email = ['email ou lista de emails']
password = "****"
message = """\
Subject: Mensagem do dia!

{}\n 
{}\n
{}\n

Essa mensagem foi gerada automaticamente pelo Python, não responder."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    print("Logando")
    server.login(sender_email, password)
    print("Enviando email")
    server.sendmail(sender_email, receiver_email, message.format(cotacao_string,temperatura,tradutor_string).encode())
    print("Fim")
    server.quit()
