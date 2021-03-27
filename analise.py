import ativo
import indicadores as ind
import fibonacci as fibo


def AnalisaEntrada(ticker):

    dados = ativo.ConsultaAtivoSemanal(ticker)
    ifr4 = ind.CalculaIFR(dados, 4)

    ifr4 = ifr4.tail(1)

    ifr = ifr4.iat[0,0]

    toque = fibo.AnalisaToqueFibo(dados)

    if toque[1] > 38.2 and ifr < 30:
        print("Entrada! IFR:"+str(ifr))
    else:
        print(toque)

    return toque
    



