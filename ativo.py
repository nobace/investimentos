import datetime as datetime
import investpy as inv
import pandas as pd
import yfinance as yf


def ConsultaAtivo(tick, country="brazil"):

    fim = datetime.date.today()
    inicio = fim - datetime.timedelta(days=600)

    dinicio = datetime.datetime.strptime(str(inicio), "%Y-%m-%d").strftime("%d/%m/%Y") 
    dfim = datetime.datetime.strptime(str(fim), "%Y-%m-%d").strftime("%d/%m/%Y")
    
    try:
      df = inv.get_stock_historical_data(tick, country,  from_date=dinicio, to_date=dfim)
      df = df[df['Open']>0]      
    except:
      try:
        if country=="brazil":
          df = yf.Ticker(tick+".SA")
        else:
          df = yf.Ticker(tick)
        df = df.history(start=inicio, end=fim, interval="1d", prepost=True)   
      except:
        df = pd.DataFrame()
        print("Erro: "+ tick)     
    return df


def ConsultaCrypto(tick):

    fim = datetime.date.today()
    inicio = fim - datetime.timedelta(days=600)

    dinicio = datetime.datetime.strptime(str(inicio), "%Y-%m-%d").strftime("%d/%m/%Y") 
    dfim = datetime.datetime.strptime(str(fim), "%Y-%m-%d").strftime("%d/%m/%Y")

    #df = yf.Ticker(tick+".SA")
    #df = df.history(start=inicio, end=fim, interval="1d", prepost=True)   
    try:
      df = inv.get_crypto_historical_data(tick, from_date=dinicio, to_date=dfim)

      df = df[df['Open']>0]      
    except:
      df = pd.DataFrame()
      print("Erro: "+ tick)     
  
    return df    

def ConsultaAtivoSemanal(tick, country='brazil'):
    df = GeraSemanal (ConsultaAtivo(tick, country))
    return df


def ConsultaCryptoSemanal(tick):
    df = GeraSemanal (ConsultaCrypto(tick))
    return df

def GeraSemanal (df):
  if (df.shape[0] > 0):
    agg_dict = {'Open': 'first',
      'High': 'max',
      'Low': 'min',
      'Close': 'last',
      'Volume': 'mean'}
  # resampled dataframe
  # 'W' means weekly aggregation
    r_df = df.resample('W').agg(agg_dict)
  else:
    r_df = df
  return r_df


