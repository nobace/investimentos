import mplfinance as mpf
import talib as ta
import pandas as pd
import indicadores as ind
from datetime import date


def GeraGraficoEntrada(periodo, dados, Papel, toque, dir):


    EMA9 = ind.CalculaEMA(dados, 9)
    EMA21 = ind.CalculaEMA(dados, 21)
    EMA50 = ind.CalculaEMA(dados, 50)    
    #EMA80 = ind.CalculaEMA(dados, 80)     
    VMA = ind.CalculaSMAVolume(dados, 20)
    IFR = ind.CalculaIFR(dados, 4)


    ap0 = [ mpf.make_addplot(EMA9,color='#FF00FF'),  # uses panel 0 by default
            mpf.make_addplot(EMA21,color='b'),  # uses panel 0 by default
            mpf.make_addplot(EMA50,color='#ffa500'),  # uses panel 0 by default
           # mpf.make_addplot(EMA80,color='#008000'),  # uses panel 0 by default            
            mpf.make_addplot(VMA,color='r', panel=1),   
        ]

    hoje = date.today()



    filename = dir + Papel + '-'+ hoje.strftime('%d-%m-%Y')+ '.png' 

    entrada = dados.iat[dados.shape[0] - 1, 1]
    stop = dados.iat[dados.shape[0] - 1, 2]
    topo = toque[2]
    fundo = toque[3]

    amplitude = topo-fundo
    r050 = topo - amplitude * 0.5
    r061 = topo - amplitude * 0.618

    p100 = stop + amplitude

    mpf.plot(
        dados,  
        title='\n'+Papel+ ' - Gráfico '+periodo,  
        ylabel='Preço',  
        type='candle', mav=(80), 
        addplot=ap0, 
        datetime_format='%d-%m-%Y',
        savefig=filename,
        figratio=(18,10),  
        #fill_between=dict(y1=entrada,y2=(entrada+0.2)),
     
        hlines=dict(hlines=[(entrada+0.01), topo, fundo, r050, r061, p100], colors=['#3366CC', '#000000', '#000000', '#FF0000', '#FF00FF', '#008000'] , linestyle='dashed', linewidths=[2, 1,1,1,1,2]),
        volume=True, 
        )


    return filename

def GeraGraficoSaida(periodo, dados, Papel, toque, dir):


    EMA9 = ind.CalculaEMA(dados, 9)
    EMA21 = ind.CalculaEMA(dados, 21)
    EMA50 = ind.CalculaEMA(dados, 50)    
    #EMA80 = ind.CalculaEMA(dados, 80)     
    VMA = ind.CalculaSMAVolume(dados, 20)
    IFR = ind.CalculaIFR(dados, 4)


    ap0 = [ mpf.make_addplot(EMA9,color='#FF00FF'),  # uses panel 0 by default
            mpf.make_addplot(EMA21,color='b'),  # uses panel 0 by default
            mpf.make_addplot(EMA50,color='#ffa500'),  # uses panel 0 by default
           # mpf.make_addplot(EMA80,color='#008000'),  # uses panel 0 by default            
            mpf.make_addplot(VMA,color='r', panel=1),   
        ]

    hoje = date.today()



    filename = dir + Papel + '-'+ hoje.strftime('%d-%m-%Y')+ '.png' 

    entrada = dados.iat[dados.shape[0] - 1, 1]
    stop = dados.iat[dados.shape[0] - 1, 2]
    topo = toque[2]
    fundo = toque[3]

    amplitude = topo-fundo
    r050 = topo - amplitude * 0.5
    r061 = topo - amplitude * 0.618

    p100 = stop + amplitude

    mpf.plot(
        dados,  
        title='\n'+Papel+ ' - Gráfico '+periodo,  
        ylabel='Preço',  
        type='candle', mav=(80), 
        addplot=ap0, 
        datetime_format='%d-%m-%Y',
        savefig=filename,
        figratio=(18,10),  
        #fill_between=dict(y1=entrada,y2=(entrada+0.2)),
     
        hlines=dict(hlines=[(entrada+0.01), topo, fundo, r050, r061, p100], colors=['#3366CC', '#000000', '#000000', '#FF0000', '#FF00FF', '#008000'] , linestyle='dashed', linewidths=[2, 1,1,1,1,2]),
        volume=True, 
        )


    return filename    