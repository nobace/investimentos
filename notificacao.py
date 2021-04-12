import telepot
import datetime as datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
  

def EnviaTextoTelegram(msg, chatid, token):
    bot = telepot.Bot(token) 
    bot.sendMessage(chatid, msg)
    return msg


def EnviaCallEntradaTelegram(mensagem, chatid, token):
    bot = telepot.Bot(token) 

    bot.sendPhoto(chatid, open(mensagem[0],'rb'))

    ganho = "{:.2f}".format(mensagem[7]-mensagem[1])
    perda = "{:.2f}".format(mensagem[1] -  mensagem[2])

    msg = mensagem[8] + ' em '+ datetime.date.today().strftime('%d/%m/%Y')+ ' atingiu a retração de Fibonacci de '+str(mensagem[4])+'% e está com IFR(5) em '+ "{:.2f}".format(mensagem[3])+'\n'
    msg += '- Compra (Entrada): Se subir acima de R$'+ "{:.2f}".format( mensagem[1]) + '\n'
    msg += '- Venda no sucesso (Alvo): R$'+ "{:.2f}".format( mensagem[7]) + ' (Ganho de R$ '+ganho+' p/ ação)\n'
    msg += '- Venda na falha (Stop): Se cair abaixo de R$'+ "{:.2f}".format( mensagem[2])  + ' (Perda de R$ '+perda+' p/ ação)\n'
    
    bot.sendMessage(chatid, msg)


def EnviaCallSaidaTelegram(mensagem, chatid, token):
    bot = telepot.Bot(token) 

    bot.sendPhoto(chatid, open(mensagem[0],'rb'))

    ganho = "{:.2f}".format(mensagem[7]-mensagem[1])
    perda = "{:.2f}".format(mensagem[1] -  mensagem[2])

    msg = mensagem[8] + ' em '+ datetime.date.today().strftime('%d/%m/%Y')+ ' atingiu a retração de Fibonacci de '+str(mensagem[4])+'% e está com IFR(5) em '+ "{:.2f}".format(mensagem[3])+'\n'
    msg += '- Compra (Entrada): Se subir acima de R$'+ "{:.2f}".format( mensagem[1]) + '\n'
    msg += '- Venda no sucesso (Alvo): R$'+ "{:.2f}".format( mensagem[7]) + ' (Ganho de R$ '+ganho+' p/ ação)\n'
    msg += '- Venda na falha (Stop): Se cair abaixo de R$'+ "{:.2f}".format( mensagem[2])  + ' (Perda de R$ '+perda+' p/ ação)\n'
    
    bot.sendMessage(chatid, msg)
