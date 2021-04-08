import pandas as pd
import analise
import notificacao as msg
import math

pasta = "C:/Users/Nob/Documents/Workspace/AnaliseFinanceira/"

#chatid = '-1001468582724'
chatid = '1226527973'
token = '1417632508:AAGgEP6emy2QeHcYJWEnOv6tc9Cgdmui6yg'


dados = pd.read_csv(pasta+'ativos.csv', sep=';')
dados = dados.dropna(subset=['TICKER'])

dados.set_index('TICKER', inplace=True)
Tickers = dados.index
print(str(Tickers))

disclaimer = 'COMPRAS DA SEMANA - SWING OU POSITION TRADE\nAs análises apresentadas a seguir são para operações de Swing ou Position Trade levando em conta, médias móveis, suportes, resistências e indicadores com o timeframe semanal para encontrar possíveis pontos de reversão da tendência de queda, por favor não utilizar esses parâmetros para Day Trade\n\n'
disclaimer +='LEGENDA DOS GRÁFICOS:\n'
disclaimer +='- Tracejado preto: indicam topo e fundo do último movimento de alta\n'
disclaimer +="- Tracejado vermelho: indica a retração de 50% em relação ao último movimento de alta\n"
disclaimer +="- Tracejado roxo: indica a retração de 61,8% em relação ao último movimento de alta\n"
disclaimer +="- Tracejado azul: indica o ponto de compra\n"
disclaimer +="- Tracejado verde: indica o ponto de venda\n"
disclaimer +="- Linha magenta: média móvel de 9 semanas\n"
disclaimer +="- Linha azul: média móvel de 21 semanas\n"
disclaimer +="- Linha laranja: média móvel de 50 semanas\n"
disclaimer +="- Linha azul claro: média móvel de 80 semanas\n\n"


#analise.AnalisaEntrada('HAPV3', pasta)

msg.EnviaTextoTelegram(disclaimer, chatid, token)

for Papel in Tickers: 
    res = analise.AnalisaEntrada(Papel, pasta, 'Semanal')
    if res[0] != '':
        msg.EnviaCallEntradaTelegram(res, chatid, token)



res = analise.AnalisaEntradaCrypto('bitcoin', pasta, 'Diario')
if res[0] != '':
    msg.EnviaCallEntradaTelegram(res, chatid, token)

res = analise.AnalisaEntradaCrypto('litecoin', pasta, 'Diario')
if res[0] != '':
    msg.EnviaCallEntradaTelegram(res, chatid, token)

#print(dados)

dados = pd.read_csv(pasta+'bdrs.csv', sep=';')
dados = dados.dropna(subset=['CÓDIGO'])

dados.set_index('CÓDIGO', inplace=True)
Tickers = dados.index
print(str(Tickers))

for Bdr in Tickers: 
    Papel = dados.at[Bdr, "TICKER"]
    if type(Papel) == str:
        res = analise.AnalisaEntradaBDR(Papel, Bdr,  pasta, 'Semanal')
        if res[0] != '':
            msg.EnviaCallEntradaTelegram(res, chatid, token)


#analise.AnalisaEntradaBDR('AAPL', 'AAPL34', pasta)