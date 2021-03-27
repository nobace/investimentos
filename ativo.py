
import datetime as datetime
import investpy as inv



def ConsultaAtivo(tick):

    fim = datetime.date.today()
    inicio = fim - datetime.timedelta(days=600)

    dinicio = datetime.datetime.strptime(str(inicio), "%Y-%m-%d").strftime("%d/%m/%Y") 
    dfim = datetime.datetime.strptime(str(fim), "%Y-%m-%d").strftime("%d/%m/%Y")

    #df = yf.Ticker(tick+".SA")
    #df = df.history(start=inicio, end=fim, interval="1d", prepost=True)   

    df = inv.get_stock_historical_data(tick, country='brazil',  from_date=dinicio, to_date=dfim)
    
    df = df[df['Open']>0]
    return df

def ConsultaAtivoSemanal(tick):
    df = GeraSemanal (ConsultaAtivo(tick))
    return df


def GeraSemanal (df):
  agg_dict = {'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last',
    'Volume': 'mean',
    'Currency': 'first'}
# resampled dataframe
# 'W' means weekly aggregation
  r_df = df.resample('W').agg(agg_dict)

  return r_df


