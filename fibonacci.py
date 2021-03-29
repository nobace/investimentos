

def get_topo_anterior (df, inicio, margem = 0.015):
  fMax = df.iat[inicio,1]
  TopoInicial = fMax
  fMin = df.iat[inicio,2]
  fPreco = df.iat[inicio,3]
  PrecoInicial = fPreco
  i = inicio - 1
  InsideBar = "N"
  j = 0
  while i > 0:
    #print(str(df.index[i])+" HighAtual="+ str(df.iat[i,1])+" < HighAnterior:"+str(fMax)+" And LowAtual="+str(df.iat[i,2])+" <= LowAnterior:"+str(fMin)+" And HighAnterior="+str(fMax)+" > HighInicial="+str(TopoInicial)+ " And PrecoAnterior="+str(fPreco)+" > PrecoInicial="+str(PrecoInicial))
    #2020-11-05 00:00:00 TopoRef=26.21 - Max:26.73 - 26.2; Min:26.11 - 25.14; InsideBar:N    
    if df.iat[i,1] < fMax and df.iat[i,2] <= fMin and fMax > TopoInicial :  #Se HighAtual < HighAnterior e LowAtual < LowAnterior e HighAnterior > HighInicial e FechamentoAnterior > Fechamento Inicial 
  #  if df.iat[i,1] < fMax and df.iat[i,2] <= fMin and fMax > TopoInicial and fPreco > PrecoInicial:  #Se HighAtual < HighAnterior e LowAtual < LowAnterior e HighAnterior > HighInicial e FechamentoAnterior > Fechamento Inicial 
        
      if InsideBar == "N":
        i += 1
      else:
        i = j  
      break
    else:
      if df.iat[i,1] > fMax :
        fMax = df.iat[i,1]
        fMin = df.iat[i,2]
        fPreco = df.iat[i,3]
        InsideBar = "N"
      else:
        if df.iat[i,1] < fMax and df.iat[i,2] > fMin:
          if InsideBar == "N":
            j = i + 1
          InsideBar = "S"
    i -= 1
  #print(str(df.index[i]))
  return i

def get_fundo_anterior (df, inicio, margem = 0.015):
  fMax = df.iat[inicio,1]
  fMin = df.iat[inicio,2]
  i = inicio - 1

  #print ('Busca a partir de '+ df.index[i].strftime('%d/%m/%Y'))

  while i > 0:
    #print(df.index[i].strftime('%d/%m/%Y') + " - Max:"+str(fMax)+" < " +str(df.iat[i,1]) + " and Min:"+str(fMin)+" < "+str(df.iat[i,2]))

    if df.iat[i,2] > fMin and df.iat[i,1] > fMax:

      #print(df.index[i].strftime('%d/%m/%Y') + " - Max2:"+str(fMax)+" < " +str(df.iat[i+2,1]) + " and Min2:"+str(fMin)+" =< "+str(df.iat[i + 2,2]))

      if (i < (inicio -1)) and df.iat[i+2,2] >= fMin :
        #print("Max1:"+str(fMax)+" - "+str(df.iat[i+2,1])+"; Min1:"+str(fMin)+" - "+str(df.iat[i+2,2]))


        i += 1
        #print('OK:'+ df.index[i].strftime('%d/%m/%Y'))
        break
      else:
        fMin = df.iat[i,2]
        fMax = df.iat[i,1]
    else:
      fMin = df.iat[i,2]
      fMax = df.iat[i,1]
    i -= 1
  #print(str(df.index[i]))
  return i


def get_topo_historico (df):
  fTopo = df['High'].idxmax()
  i = df.index.get_loc(fTopo)
  #print("Maximo:"+str(i))
  return i

def get_fundo_historico (df):
  fFundo = df['Low'].idxmin()
  i = df.index.get_loc(fFundo)
  #print("Minimo:"+str(fFundo))
  return i


def ProcuraCandleMenor (df, inicio, valor):
  i = inicio

  while i > 0 and df.iat[i,2] > valor:
    i -= 1
  return i


def AnalisaRetracaoFibo(Preco, Topo, Fundo):
  resultado = ['', 0.0]
  Diff = Topo - Fundo
  #print('Preço: ' + str(PrecoRef))

  F38 = Topo - Diff * 0.382
  F50 = Topo - Diff * 0.50
  F61 = Topo - Diff * 0.618 

  resultado[0] = '- Não foi identificado toque em nenhuma retração de Fibonacci (Última pernada de alta - Topo:'+str(Topo)+' Fundo:'+str(Fundo)+')\n'
  if Preco <= F61:
    resultado[0] = '- Tocou a retração de 61,8% (Última pernada de alta - Topo:'+str(Topo)+' Fundo:'+str(Fundo)+')\n  A ação devolveu 61,8% do valor da última subida sendo uma oportunidade de pegar uma nova sequência de altas caso o papel tenha uma reação\n'  
    resultado[1] = 61.8
  else:
    if Preco <= F50:
      resultado[0] = '- Tocou a retração de 50% (Última pernada de alta - Topo:'+str(Topo)+' Fundo:'+str(Fundo)+')\n  A ação devolveu 50% do valor da última subida sendo uma oportunidade de pegar uma nova sequência de altas caso o papel tenha uma reação\n'  
      resultado[1] = 50
    else:
      if Preco <= F38:
        resultado[0] = '- Tocou a retração de 38,2% (Última pernada de alta - Topo:'+str(Topo)+' Fundo:'+str(Fundo)+')\n  A ação devolveu 38,2% do valor da última subida, o que costuma ser pouco a não ser que o papel esteja muito com uma tendência de alta muito forte. O normal seria aguardar para entrar apenas quando atingir 50% ou 61,8%\n'  
        resultado[1] = 38.2

  return resultado



def AnalisaToqueFibo(df):
  resultado = [
                 '',  #Texto
                 0.0, #Perc. Retração
                 0.0, #Topo
                 0.0, #Fundo
                 0,   #Indice Topo
                 0    #Indice Fundo
              ]
  last = df.shape[0] - 1

  i = get_topo_anterior(df, last)
  #print ('Topo 1:'+df.index[i].strftime('%d/%m/%Y') +' --- '+ str(df.iat[i,1]))
  if i == last - 1:
    i = get_topo_anterior(df, i)

  j = ProcuraCandleMenor (df, i, df.iat[last,2])
  k = get_fundo_anterior(df, j+1)

  dfAux = df.tail(last - i)
  l = get_fundo_historico (dfAux)
  fundoRef = dfAux.iat[l,2]
  #print ('Desconto: '+str(last - i)+' Topo:'+df.index[i].strftime('%d/%m/%Y') + ' Fundo:'+dfAux.index[l].strftime('%d/%m/%Y'))

  while df.iat[k,2] > fundoRef and k > 0:
    k -= 1
    k = get_fundo_anterior(df, k)
    #print ('Topo:'+df.index[i].strftime('%d/%m/%Y') + ' Fundo:'+df.index[k].strftime('%d/%m/%Y'))

  dfAux = df.tail(last - k)
  l = get_topo_historico (dfAux)

  
  #print ('Topo:'+df.index[i].strftime('%d/%m/%Y') + ' Fundo:'+df.index[k].strftime('%d/%m/%Y'))


  #print ('Fundo a partir de '+ df.index[j+1].strftime('%d/%m/%Y') +':'+str(df.iat[k,2]))

  saida = AnalisaRetracaoFibo(df.iat[last,2], dfAux.iat[l,1], df.iat[k,2])
  resultado[0] = saida[0]
  resultado[1] = saida[1]
  resultado[2] = dfAux.iat[l,1]
  resultado[3] = df.iat[k,2]
  resultado[4] = l #Indice topo
  resultado[5] = k #Indice fundo
  

  #print ('Resultado:'+ resultado)
  return resultado