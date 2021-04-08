#Bibliotecas nativas do Python.
import os 
import time
import re

#Bibliotecas que nós instalamos.
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver


class wppbot:
#Setamos o caminho de nossa aplicação.
    dir_path = os.getcwd()
#Nosso contrutor terá a entrada do nome do nosso 
    def __init__(self, nome_bot):
#Setamos nosso bot e a forma que ele irá treinar.
        self.bot = ChatBot(nome_bot)
        self.bot.set_trainer(ListTrainer)
#Setamos onde está nosso chromedriver.
        self.chrome = self.dir_path+'\\chromedriver\\chromedriver.exe'

        print(self.chrome)
#Configuramos um profile no chrome para não precisar logar no whats toda vez que iniciar o bot.
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir="+self.dir_path+"\profile\wpp")
#Iniciamos o driver.
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)


    def inicia(self,nome_contato):
    #Selenium irá entrar no whats e aguardar 15 segundos até o dom estiver pronto.
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)
    #Selecionamos o elemento da caixa de pesquisa do whats pela classe.
        self.caixa_de_pesquisa = self.driver.find_element_by_class_name('jN-F5')

    #Escreveremos o nome do contato na caixa de pesquisa e aguardaremos 2 segundos.
        self.caixa_de_pesquisa.send_keys(nome_contato)
        time.sleep(2)
    #Vamos procurar o contato/grupo que está em um span e possui o título igual que buscamos e vamos clicar.   
        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
        self.contato.click()
        time.sleep(2)


dir_path = os.getcwd()
print(dir_path)