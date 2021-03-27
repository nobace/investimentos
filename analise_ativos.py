import pandas as pd
import analise

pasta = "C:/Users/Nob/Documents/Workspace/AnaliseFinanceira/"

dados = pd.read_csv(pasta+'ativos.csv', sep=';')
dados = dados.dropna(subset=['TICKER'])

dados.set_index('TICKER', inplace=True)
Tickers = dados.index
print(str(Tickers))

for Papel in Tickers: 
    analise.AnalisaEntrada(Papel, pasta)


#print(dados)