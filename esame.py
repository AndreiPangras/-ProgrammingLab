#======================
# Classe per file CSV
#======================

class CSVTimeSeriesFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name

    def get_data(self,):     
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            
            # Esco dalla funzione tornando "niente".
            return None
        lista_gen=[]
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            #tolgo da ogni riga lo spazio
            string=line.strip('\n')
            #divido la stringa 
            elements = string.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'epoch':
                # Setto l'epoche  ed il valore
                epoch = elements[0]
                temp= elements[1]
          #Crea una lista e inserisco la mia lista appena creata
                lista_gen.append([epoch,temp])
  
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return lista_gen
    
       

class ExamException(Exception):

    pass

#======================
# Corpo del programma
#======================

def  hourly_trend_changes(time_series ):
    #inizializzo dei vettori vuoti per 
    #le temperature
    #le epoche convertite 
    #e per una lista dove salvo i diversi valori delle ore 
    lista_ore=[]
    lista_temp=[]
    cont=0
    lista_indici=[]
    for item in time_series:
        #salvo i dati separandoli tra epoche e temperature
        epoch=float(item[0])
        temperature=float(item[1])


      #controllo che nel epoch e nelle temperature ci sia qulcosa
        if(epoch==' '):
            continue
        elif(temperature==' '):
            continue
        else:
            try:
                #transformo le emopoche in int in caso non lo fossero
                # e divido per trovare il numero di ore 
                ora=(int(epoch)/3600)
                #tramite round arrotondo il valore con una cifra decimale 
                tempo=round(ora,1)
            except Exception as e:              
                # Stampo l'errore
                print('Errore nela conversione da epoch in ore int : "{}"'.format(e))          

            #prendola variabile tempo e la trasfonrma in una stringa
            #per poi splittarla cosi da avvere piu facilita nel fare i controllli dopo
            try:
                #converto le epoch da int a stringa 
                #cosi da poter dividerle e prender solo un numero intero
                tempo=str(tempo)
            except Exception as e:
                print('Errore nella conversione del tempo da int a stringa: "{}"'.format(e))

            num=tempo.split('.')

            intero=num[0]

            try:
                #converto le temperature in float se non lo fossero gia 
                temperature = float(temperature)
            except Exception as e:              
                # Stampo l'errore
                print('Errore nela conversione a float: "{}"'.format(e))          
                # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                #----------------------------
                #chiedi a sta del continue 
                #------------------------------
                continue
            intero.strip( )
      
            if(cont==0):
                lista_ore.append(intero)
                lista_indici.append(intero)
                cont+=1
            elif(intero==lista_ore[cont-1]):
                lista_ore.append(intero)
                cont+=1
            else:
                lista_indici.append(intero)
                lista_ore.append(intero)
                cont+=1

        lista_temp.append(temperature)
      

    #return lista_indici
    numero=0
    lista_celsius=[]  
    for i in lista_indici:
        lista_temporale=[]
        #vedo qualte volte mi si ripete un ora e qunad'e la prima volta che trovo quel dato
        #---------------------------------------------
        #errore  nel count e index
        #--------------------------------------------
        controllo=lista_indici[numero]

        ricerca=lista_ore.index(controllo)
        contatore=lista_ore.count(controllo)
        punt=ricerca+contatore

        if(contatore!=1):
            if(ricerca!=0):
                temporanea=lista_temp[ricerca-1]
                lista_temporale.append(temporanea)
                while ricerca<punt:
                    val=lista_temp[ricerca]
                    lista_temporale.append(val)
                    ricerca+=1
            else:
                while ricerca<contatore:
                  val=lista_temp[ricerca]
                  lista_temporale.append(val)
                  ricerca+=1
        else: 
          if(ricerca!=0):

              temporanea_pre=lista_temp[ricerca-1]
              temporanea_suc=lista_temp[ricerca+1]
              val=lista_temp[ricerca]
              lista_temporale.append(temporanea_pre)
              lista_temporale.append(val)
              lista_temporale.append(temporanea_suc)
          else:
              val=lista_temp[ricerca]
              lista_temporale.append(val)
                
        numero+=1
        lista_celsius.append(lista_temporale)
    #return lista_celsius

    #mi restituisce le temperature ragggruppate per ore
    #return lista_celsius
    incremento=0
    #lista dove vengono visulaizzati i trend
    lista_finale=[]
    direz_prev=None
    for item in lista_celsius:
        #incremento e il val che punta in lista_celsius
        val=lista_celsius[incremento]
        lung_lista=(len(val))-1
        #direzzione creascente = True
        #direzoine decrescente = False
        i=0
        trend=0
        #print(val) va tutot bene
        if(val[i]==val[i+1]):
            i+=1
            prev_direz=direz_prev
        else: 
            if(val[i]<val[i+1]):
                prev_direz= True
                i+=1
            else:
                prev_direz= False
                i+=1
            if(direz_prev!=prev_direz)and (direz_prev!=None):
                trend+=1


        #temp_direz= False
        
        while i<lung_lista:
            if(val[i]==val[i+1]):
                temp_direz=prev_direz
            elif(val[i]<val[i+1]):
                temp_direz= True
            else:
                temp_direz=False

            if(prev_direz!=temp_direz)and prev_direz!=None:
                prev_direz=temp_direz
                trend+=1

            i+=1
        direz_prev=prev_direz
        incremento+=1
        lista_finale.append(trend)

    return lista_finale
    #return lista_celsius

       
       
    

  

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(hourly_trend_changes(time_series))

