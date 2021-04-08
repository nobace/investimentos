import ativo
import indicadores as ind
import fibonacci as fibo
import graficos as g


def AnalisaEntrada(ticker, pasta, periodo='Semanal'):
    print("Analisando "+ ticker)
    pastaImagens= pasta + '/imagens/entradas/'+periodo+'/'
    resultado = [ '',  #0 - Imagem grafico
                  0.0, #1 - Entrada
                  0.0, #2 - Stop
                  0.0, #3 - IFR
                  0.0, #4 - Retracao Fibo
                  0.0, #5 - Preço Alvo 1
                  0.0, #6 - Preço Alvo 2
                  0.0, #7 - Preço Alvo 3
                  ''   #8 - Ticker                  
    ]

    if periodo == 'Semanal':
        dados = ativo.ConsultaAtivoSemanal(ticker)
    else:
        dados = ativo.ConsultaAtivo(ticker)        
    tamanho = dados.shape[0]
    print(str(tamanho))
    if tamanho >= 80:
        ifr5 = ind.CalculaIFR(dados, 5)

        ifr5 = ifr5.tail(1)

        ifr = ifr5.iat[0,0]

        mm9 = ind.CalculaEMA(dados, 9)
        mm9 = mm9.tail(1)
        vmm9 = mm9.iat[0,0]


        mm80 = ind.CalculaSMA(dados, 80)
        mm80 = mm80.tail(1)
        vmm80 = mm80.iat[0,0]

        toque = fibo.AnalisaToqueFibo(dados)

        if toque[1] > 38.2 and ifr <= 30 and vmm9 > vmm80:
            print("Entrada! IFR:"+str(ifr))

            entrada = dados.iat[dados.shape[0] - 1, 1] + 0.01
            stop = dados.iat[dados.shape[0] - 1, 2]

            topo = toque[2]
            fundo = toque[3]

            amplitude = topo-fundo
            p050 = stop + amplitude * 0.5
            p061 = stop + amplitude * 0.618
            p100 = stop + amplitude 

            resultado[0] = g.GeraGraficoEntrada(periodo, dados, ticker, toque, pastaImagens)
            resultado[1] = entrada
            resultado[2] = stop
            resultado[3] = ifr
            resultado[4] = toque[1]
            resultado[5] = p050
            resultado[6] = p061
            resultado[7] = p100
            resultado[8] = ticker
        else:
            print(toque)

    return resultado


def AnalisaEntradaCrypto(ticker, pasta, periodo='Semanal'):
    print("Analisando "+ ticker)
    pastaImagens= pasta + '/imagens/entradas/'+periodo+'/'
    resultado = [ '',  #0 - Imagem grafico
                  0.0, #1 - Entrada
                  0.0, #2 - Stop
                  0.0, #3 - IFR
                  0.0, #4 - Retracao Fibo
                  0.0, #5 - Preço Alvo 1
                  0.0, #6 - Preço Alvo 2
                  0.0, #7 - Preço Alvo 3
                  ''   #8 - Ticker                  
    ]

    if periodo == 'Semanal':
        dados = ativo.ConsultaCryptoSemanal(ticker)
    else:
        dados = ativo.ConsultaCrypto(ticker)     
    tamanho = dados.shape[0]
    print(str(tamanho))
    if tamanho >= 80:
        ifr5 = ind.CalculaIFR(dados, 5)

        ifr5 = ifr5.tail(1)

        ifr = ifr5.iat[0,0]

        mm9 = ind.CalculaEMA(dados, 9)
        mm9 = mm9.tail(1)
        vmm9 = mm9.iat[0,0]


        mm80 = ind.CalculaSMA(dados, 80)
        mm80 = mm80.tail(1)
        vmm80 = mm80.iat[0,0]

        toque = fibo.AnalisaToqueFibo(dados)

        if toque[1] > 38.2 and ifr <= 30 and vmm9 > vmm80:
            print("Entrada! IFR:"+str(ifr))

            entrada = dados.iat[dados.shape[0] - 1, 1] + 0.01
            stop = dados.iat[dados.shape[0] - 1, 2]

            topo = toque[2]
            fundo = toque[3]

            amplitude = topo-fundo
            p050 = stop + amplitude * 0.5
            p061 = stop + amplitude * 0.618
            p100 = stop + amplitude 

            resultado[0] = g.GeraGraficoEntrada(periodo, dados, ticker, toque, pastaImagens)
            resultado[1] = entrada
            resultado[2] = stop
            resultado[3] = ifr
            resultado[4] = toque[1]
            resultado[5] = p050
            resultado[6] = p061
            resultado[7] = p100
            resultado[8] = ticker
        else:
            print(toque)

    return resultado

def AnalisaEntradaBDR(ticker, bdr, pasta, periodo='Semanal'):

    pastaImagens= pasta + '/imagens/entradas/'+periodo+'/'
    resultado = [ '',  #0 - Imagem grafico
                  0.0, #1 - Entrada
                  0.0, #2 - Stop
                  0.0, #3 - IFR
                  0.0, #4 - Retracao Fibo
                  0.0, #5 - Preço Alvo 1
                  0.0, #6 - Preço Alvo 2
                  0.0, #7 - Preço Alvo 3
                  ''   #8 - Ticker                  
    ]

    if type(ticker) == str and type(bdr) == str:
        print("Analisando "+ str(ticker))
        if periodo == 'Semanal':
            dados = ativo.ConsultaAtivoSemanal(ticker, 'united states')
            dados2 = ativo.ConsultaAtivoSemanal(bdr)
        else:
            dados = ativo.ConsultaAtivo(ticker, 'united states')
            dados2 = ativo.ConsultaAtivo(bdr)

        tamanho = dados.shape[0]
        tamanho2 = dados2.shape[0]    
        print("Tam Ação:"+str(tamanho))
        print("Tam BDR:"+str(tamanho2))

        if tamanho >= 80 and tamanho2 >=80 :
            ifr5 = ind.CalculaIFR(dados, 5)

            ifr5 = ifr5.tail(1)

            ifr = ifr5.iat[0,0]

            mm9 = ind.CalculaEMA(dados, 9)
            mm9 = mm9.tail(1)
            vmm9 = mm9.iat[0,0]


            mm80 = ind.CalculaSMA(dados, 80)
            mm80 = mm80.tail(1)
            vmm80 = mm80.iat[0,0]

            toque = fibo.AnalisaToqueFibo(dados)
            toque2 = fibo.AnalisaToqueFibo(dados2)


            if toque[1] > 38.2 and ifr <= 30 and vmm9 > vmm80:
                print("Entrada! IFR:"+str(ifr))

                entrada = dados2.iat[dados2.shape[0] - 1, 1] + 0.01
                stop = dados2.iat[dados2.shape[0] - 1, 2]

                topo = toque2[2]
                fundo = toque2[3]

                amplitude = topo-fundo
                p050 = stop + amplitude * 0.5
                p061 = stop + amplitude * 0.618
                p100 = stop + amplitude 

                resultado[0] = g.GeraGraficoEntrada('Semanal', dados2, bdr, toque2, pastaImagens)
                resultado[1] = entrada
                resultado[2] = stop
                resultado[3] = ifr
                resultado[4] = toque2[1]
                resultado[5] = p050
                resultado[6] = p061
                resultado[7] = p100
                resultado[8] = bdr
            else:
                print(toque)
    else:
        print("Ticker inválido")
    return resultado


#res = AnalisaEntrada("RENT3")


def AnalisaSaida(ticker, qtd, vCompra, pasta):
    pastaImagens= pasta + '/imagens/saidas/'
    resultado = [ '',  #0 - Imagem grafico
                  0.0, #1 - Saida
                  0.0, #2 - Lucro
                  ''   #8 - Ticker                  
    ]

    dados = ativo.ConsultaAtivoSemanal(ticker)
    tamanho = dados.shape[0]

    #print("Tam:"+str(tamanho))
    
    if tamanho >= 12:
        ifr5 = ind.CalculaIFR(dados, 5)
        #Calcula IFR(5) Semana atual
        ifrAtual = ifr5.iat[ifr5.shape[0]-1, 0]
        #Calcula IFR(5) Semana anterior
        ifrAnt = ifr5.iat[ifr5.shape[0]-2, 0]

        #Se IFR(5) Anterior > 70 e IFR(5) Atual < 70, o ponto de saída é na perda da minima da semana atual
        if ifrAtual > 70 or ifrAnt > 70:
            print("Analisando "+ ticker)            
            print("IFR Atual: "+str(ifrAtual))
            print("IFR Ant:" +str(ifrAnt)+'\n')

        if ifrAnt > 70 and ifrAtual < ifrAnt:
            saida = dados.iat[dados.shape[0] - 1, 2]
            print("Saída em "+str(saida)+'\n')

     