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

            string=line.strip('\n')
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

    lista_ore=[]
    lista_temp=[]
    for item in time_series:

      epoch=(item[0]).strip('\n')
      temperature=(item[1]).strip('\n')

      try:
          ora=(int(epoch)/3600)
          tempo=round(ora,1)
      except Exception as e:              
          # Stampo l'errore
          print('Errore nela conversione da epoch in ore int : "{}"'.format(e))          

        #prendola variabile tempo e la trasfonrma in una stringa
        #per poi splittarla cosi da avvere piu facilita nel fare i controllli dopo
      try:
          tempo=str(tempo)
      except Exception as e:
          print('Errore nella conversione del tempo da int a stringa: "{}"'.format(e))

      num=tempo.split('.')

      intero=num[0]
      try:
          temperature = float(temperature)
      except Exception as e:              
          # Stampo l'errore
          print('Errore nela conversione a float: "{}"'.format(e))          
          # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
          continue

      lista_ore.append(intero)
      lista_temp.append(temperature)

    #return lista_ore
    #return lista_temp

#-------------------------------------------------------
#creazione di liste con le ore e le temperature riuscita


    # seleziona ogni item/lista... basta che la fai puntare con un for ....
    #fai slip di quello chai hai e tiritrovi una stringa 
    #la fai un valore intero con round()
    #devi usare una variabile di appoggi che tine c0nto in che posizione e il tuo epoch 
    #devi creare un modello trend per trovare poi che temp dovrebbe essere

#prendi la lunghezza della lista per poi prendere unoa a una le lista .. transformarle in stringhee 
#dividerle tramite split()
#selezionare cosi l'epoche/3600
#cosi da avere le ore .. confronta le epoche con lo stesso numero di ore 
#selezionando cosi le sudette tmperatura 
#per poi creare un modello di previsione e in caso 
#sia sbagliato auumentare di uno un contatore che ceh alla fine dei dati di un Ora
#scriva in una lista i valori 
#


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(hourly_trend_changes(time_series))
#print(time_series )


