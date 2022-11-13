import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from datetime import date


response = requests.get('https://alternative.me/crypto/fear-and-greed-index/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

medo_mercado = site.find('div', attrs={'class': 'fng-circle'})
medo_texto = site.find('div', attrs={'class': 'status'})
medo = int(medo_mercado.text)

data = date.today()

email_adress = 'robomensageiro4321@gmail.com'
destinatario = 'arlisson234529@gmail.com'
senha = 'ciounqbgujbtumly'
mensagem = 'O mercado de cripto está em {}, o termômetro está no número: {}\n\nAtenciosamente Fábrica de Software so Instituto Federal Fluminense\nData:{}/{}/{}'.format(
    medo_texto.text, medo, data.day, data.month, data.year)


if(medo <= 20):
    msg = EmailMessage()
    msg['Subject'] = 'Atualização Sobre o Mercado de Cripto'
    msg['From'] = email_adress
    msg['To'] = destinatario
    msg.set_content(mensagem)
else:
    msg = EmailMessage()
    msg['Subject'] = 'Atualização Sobre o Mercado de Cripto'
    msg['From'] = email_adress
    msg['To'] = destinatario
    msg.set_content(mensagem)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_adress, senha)
    smtp.send_message(msg)
