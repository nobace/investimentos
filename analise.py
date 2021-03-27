import ativo
import indicadores as ind
import fibonacci as fibo
import graficos as g


def AnalisaEntrada(ticker, pasta):
    print("Analisando "+ ticker)
    pastaImagens= pasta + '/imagens/'

    dados = ativo.ConsultaAtivoSemanal(ticker)
    tamanho = dados.shape[0]
    print(str(tamanho))
    if tamanho >= 80:
        ifr4 = ind.CalculaIFR(dados, 4)

        ifr4 = ifr4.tail(1)

        ifr = ifr4.iat[0,0]

        mm9 = ind.CalculaEMA(dados, 9)
        mm9 = mm9.tail(1)
        vmm9 = mm9.iat[0,0]


        mm80 = ind.CalculaSMA(dados, 80)
        mm80 = mm80.tail(1)
        vmm80 = mm80.iat[0,0]

        toque = fibo.AnalisaToqueFibo(dados)

        if toque[1] > 38.2 and ifr < 30 and vmm9 > vmm80:
            print("Entrada! IFR:"+str(ifr))
            g.GeraGraficoEntrada('Semanal', dados, ticker, toque, pastaImagens)
        else:
            print(toque)
    else:
        toque = [ '', 0.0, 0.0, 0.0, 0, 0]

    return toque
    

#res = AnalisaEntrada("RENT3")



