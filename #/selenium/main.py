from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

#pessoas que deseja enviar as mensagens
contatos = ['5543998430129', '5543984991729']
#Grupos que deseja pegar os contatos
grupos = []
#Mensagem a ser enviada
mensagem = 'Isto é apenas um teste'
mensagem = urllib.parse.quote(mensagem)

def send_mensage(contato, mensagem):
    driver.get('https://web.whatsapp.com/')
    link_mensagem = f'https://web.whatsapp.com/send?phone={contato}&text={mensagem}'
    if len(driver.find_element_by_id('side')) > 1:
        driver.get(link_mensagem)


def phishing_contatcs(grupo):
    pass

for c in contatos:
    send_mensage(c, mensagem)
    print(f'Mensagem enviada [ {c} ]')
    print()
