#======================
# Classe per file CSV
#======================

class CSVTimeSeriesFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name

    def get_data(self):     
      #provo ad aprire il file in modalita lettura
        try:
            my_file = open(self.name, 'r')
        except:
           # Concludo il programma 
            raise ExamException('Errore nell apertura del  file')
              
        #inizializzo una lista vuota
        lista_gen=[]
        # Ora inizio a leggere il file linea per linea
        for i, line in enumerate(my_file):
            #tolgo da ogni riga lo spazio
            string=line.strip('\n')
            #divido la stringa 
            elements = string.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'epoch':
                #provo a tranformare l'epoch da una stringa a un float
                #poi la arrotondo con il metodo round
                try:
                    epoch =round(float(elements[0]))
                except:
                    continue
                #provo a transformare le temperature in float 
                try:
                     temp= float(elements[1])
                except:
                    continue

          #riempio la mia lista inserendo l'epoch e le temperature
          #creando cosi una lista con delle liste 
                lista_gen.append([epoch,temp])
  
        # Chiudo il file
        my_file.close()
        #creo un ciclo per controllare
        # se sono presenti dei valori (epoch) dupplicati  o fuori ordine 
        for i,line in enumerate(lista_gen):
          #salto il primo valore
            if (i==0):
              continue
              #controllo che in posizione attuale non ci sia un valore identico a quello precedente 
              #inoltre controllo che nella posizione attuale non ci sia un valore piu piccolo di quello precedente
            if i>1:
                if(lista_gen[i][0]<=lista_gen[i-1][0]):

                    raise ExamException('Nella lista sono presenti dei  valori fuori ordine oppure dupplicati')


        
        # Mi torna la lista una volta riempita
        return lista_gen
    
       

class ExamException(Exception):

    pass

#======================
# Corpo del programma
#======================

def  hourly_trend_changes(time_series ):
    #inizializzo delle liste vuoti per 
    #le temperature
    #le epoche convertite in ore
    #e per una lista dove salvo i diversi valori delle ore 
    lista_ore=[]
    lista_temp=[]
    cont=0
    lista_indici=[]
    for item in time_series:
        #salvo i dati separandoli tra epoche e temperature
        epoch=item[0]
        temperature=item[1]


      #controllo che nel epoch e nelle temperature ci sia qulcosa
        if(epoch==' '):
            continue
        elif(temperature==' '):
            continue
        else:
            try:
                #transformo le epoch da secondi a ore dividendo per 3600
                #tramite round arrotondo il valore con una cifra decimale 
                ora=(epoch)/3600
                ora=round(ora,1)
            except Exception as e:              
                # Stampo l'errore
                print('Errore nela conversione dei secondi del epoch a ore  : "{}"'.format(e))          

            #prendo la variabile tempo e la trasfonrma in una stringa
            #per poi splittarla cosi da avvere un valore intero di ore da poter gestire 
            try:
                #converto le epoch da float a stringa 
                #cosi da poter dividerle e prender solo un numero intero
                ora=str(ora)
            except Exception as e:
                print('Errore nella conversione delle ore da float a string: "{}"'.format(e))

            num=ora.split('.')

            intero=num[0]
            #utilizzo il comando strip per togli possibili spazzi
            intero.strip( )
            #controllo il valore di cont( che e un mio contatore)
            #che viene usato per vedere la prima volta che inserisco i dati
            #cosi da riuscire a riempire 2 liste 
            #la prima cioe la lista_ore dove io salvo tutte le epoch transformate in ore
            #la seconda dove salvo solamente un unica volta l'ora
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
        #inserisco la lista con le temperature
        lista_temp.append(temperature)
      

   
    lista_celsius=[]  
    for i,line in enumerate(lista_indici):
        lista_temporale=[]
        #salvo in un variabile il valore preso dalla lista indici
        controllo=lista_indici[i]
        #creo 2 variabile
        #la prima che contiene posizione dove io incontro il valore che sto considerando
        #la seconda che contiene quante volte e presente nel file il valore
        ricerca=lista_ore.index(controllo)
        contatore=lista_ore.count(controllo)
        #la varibile punt e una varibile che contine la somma tra ricerca e contatore
        punt=ricerca+contatore
        #per prima cosa controllo che ci sia piu di un valore 
        #poi controllo se la sua posizione e diversa da 0, qundi che non sia il primo elemento
        if not (contatore==1):
            if not (ricerca==0):
              #se la sua posizione e diversa da zero 
              #allora prima di iniziare ad aggiungere le varie temperature rigurdante l'ora che sto considerando
              #creo una variabile dove mi salvo l'ultima temperatura rergistrata del ora prima
              #fatto cio  inserisco nella mia lista la variabile (che contiene l'ultima temperatura dell'ora precedente registrata ) e poi anche  tutte le temperature riguardanti quel ora
                temporanea=lista_temp[ricerca-1]
                lista_temporale.append(temporanea)
                while ricerca<punt:
                    val=lista_temp[ricerca]
                    lista_temporale.append(val)
                    ricerca+=1
            else:
                #se invece la prima posizione del ora che io sto considerando e 0
                #allora inserisco semprecemente i valori del ora che sto gestendo
                while ricerca<contatore:
                  val=lista_temp[ricerca]
                  lista_temporale.append(val)
                  ricerca+=1
        else: 
          #nel caso ci fosse solo una varibile allora 
          #controlla prima di tutto se la sua posizione e diversa da 0
          if not(ricerca==0):
              #se e diversa da 0 non faccio altro che prendere il valore del ora precedente
              #e inserirlo nella mia lista per poi aggiungere quel unica temperatura che ho  
              temporanea_pre=lista_temp[ricerca-1]
              val=lista_temp[ricerca]
              lista_temporale.append(temporanea_pre)
              lista_temporale.append(val)

          else:
            # in caso il nostro vcalore fosse unico elemento
            #si trovasse nella prima posizione allora 
            #aggiungiamo solo questo valore senza fare altro
              val=lista_temp[ricerca]
              lista_temporale.append(val)
                
       
        #inserisco in una lista , la mi lista con tutte  le temperature
        #da prendere in considerazione per calcolare il trend per ogni ora
        lista_celsius.append(lista_temporale)
 


    incremento=0
    lista_finale=[]
    direz_vett=None
    #creo un ciclo per il calcolo del trend ora per ora 
    for item in lista_celsius:
        #la varibile val contine la mia lista con tutte le temperature di un ora
        #infatti ogni volta in base alla variabile incremento punta un altra lista di temperature 
        val=lista_celsius[incremento]
        #creo una varibile che contine la lungheezza della lista -1 
        #facendo cosi arrivo al penultimo elemento che verra confrontato con l'ultimo
        lung_lista=(len(val))-1
        #direzzione creascente = True
        #direzoine decrescente = False
        i=0
        trend=0
        #controllo che la temperatura nella posizione attulae sia uguale alla temperatura successiva
        if(val[i]==val[i+1]):
          #nel caso fosse vero
          #incremento il mio puntatore cosi che i controli li inizi a fare quando vale 1
          #e in piu salvo nella direzione del mio vettore
          # la direzione prevista cosi mantengo l'andamento precedentemente ottenuto
            i+=1
            prev_direz=direz_vett
        else: 
          #se non sono uguali allora controllo
          # se il valore nella posizione attuale sia mionore del valore nella prossima posizione
            if(val[i]<val[i+1]):
              #se e vero allora imposto il mio andamento a true ( crescente)
                prev_direz= True
                i+=1
            else:
              #se invece non e minore imposto il mio andamento a False(decrescente)
                prev_direz= False
                i+=1
                #alla fine di tutto controllo 
                #se la direzione ottenuta dalla lista precedente e diversa da quella attuale
                #e controllo se e diversa dal vuoto
                # se succede allora io so gia che nella primo valore che di quel ora ce un cambio 
                #dell'andamento
            if not(direz_vett==prev_direz)and not (direz_vett==None):
                trend+=1



        #inizio a controllare un elemento alla volta 
        #prima di tutto controllo se sono uguali allora
        # in quel caso l'andamento che io ho previsto sara ugulae al andamento dell'ora
        #se non fosse faccio i sudetti conroli per vedere che andamento prendono le temperature
        while i<lung_lista:
            if(val[i]==val[i+1]):
                temp_direz=prev_direz
            elif(val[i]<val[i+1]):
                temp_direz= True
            else:
                temp_direz=False
              #controllo sel l'andamento previsto da me e diverso dall'andamento che hanno adesso le temperature
              #inoltre controllo anche che la direzione prevista non sia vuota
              #se queste afermazione sono vera allora ho un cambiamento nel mio andamento 
              #e aumento di 1 il mio trend
              #poi cambio la mia previsione del andamento 
              #e la metto uguale all'andamento che hanno adesso le tempemperature
            if not(prev_direz==temp_direz)and not (prev_direz==None):
                prev_direz=temp_direz
                trend+=1

            i+=1
            #una volta finita la mia lista di temperature per quel'ora specifica
            #salvo l'ultimo andamento che hanno avuto le temperature di quest'ora nella direzione prevista
        direz_vett=prev_direz
        incremento+=1
        #inserisco nella mia lista il valore del trend
        lista_finale.append(trend)

    return lista_finale

        

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(hourly_trend_changes(time_series))

