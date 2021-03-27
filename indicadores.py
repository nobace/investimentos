import talib as ta
import pandas as pd

#Cria o DataFrame da media movel exponencial
def CalculaEMA(df,window=7,colum='ema'):
    emas = ta.EMA(df['Close'],window)
    #Cria o DataFrame com os valores da media movel e usa a data como indice
    emas = pd.DataFrame(data = emas, index = df.index, columns = [colum])
    return emas

#Cria o DataFrame da media movel simples
def CalculaSMA(df,window=7,colum='sma'):
    smas = ta.SMA(df['Close'],window)
    #Cria o DataFrame com os valores da media movel e usa a data como indice
    smas = pd.DataFrame(data = smas, index = df.index[(window-1):], columns=[colum])

    return smas

#Cria o DataFrame do indice de força relativa
def CalculaIFR(df,window=7,colum='ifr'):
    #retorna o indice de força relativa 
    ifrs = ta.RSI(df['Close'],window)
     #Cria o DataFrame com os valores da media movel e usa a data como indice
    ifrs = pd.DataFrame(data = ifrs, index = df.index[(window):], columns=[colum])
    return ifrs


#Cria o DataFrame da media movel simples
def CalculaSMAVolume(df,window=20,colum='sma'):

    print(df['Volume'])
    vmas = ta.SMA(df['Volume'],window)
    #Cria o DataFrame com os valores da media movel e usa a data como indice
    vmas = pd.DataFrame(data = vmas, index = df.index, columns = [colum])

    return vmas