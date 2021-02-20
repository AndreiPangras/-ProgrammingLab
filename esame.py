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
    cont=0
    lista_indici=[]
    for item in time_series:

      epoch=item[0]
      temperature=item[1]
      temperature=temperature.strip()

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
      
      intero.strip()
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
      #controllo se la lista e vuota .. se vuota non faccio ninete ..
      #se non lo e
      #potrei controllar4e che la mia item siua uguale alla  precedentemente inserito in lista .. 
      #quando e diverso creo una lista e metto dentro a mo di stringa l'item
      #cosi da poterlo usare dopo per fare la ricerca 
      #cosidero un contatore che ogni volta che inserisco amumenta di 1 
      #fino a quando non rovo che sono diversi .. e li devo 
      #controllare tramite index la ricerca dellla prima volta che hanno insierto il mio valore
      #fare val-1 e vedere se esiste .. se no ... allora considero solo le posizioni che ho 
      #se invece essite prendo anche quel valore per fare il trend 
    i=0
    lista_celsius=[]  
    for item in lista_indici:
        lista_tomporale=[]
        #vedo qualte volte mi si ripete un ora e qunad'e la prima volta che trovo quel dato
        ricerca=lista_ore.index(lista_indici[i])
        contatore=lista_ore.count(lista_indici[i])

        if(ricerca!=0):
            temporanea=lista_temp[ricerca-1]
            while ricerca<contatore:
              val=lista_temp[ricerca]
              lista_tomporale.append(temporanea,val)
              ricerca+=1

        else:

            while ricerca<contatore:
                val=lista_temp[ricerca]
                lista_tomporale.append(val)
                ricerca+=1
        i+=1
        lista_celsius.append(lista_tomporale)

    return lista_celsius




      


      
    
    #return len(lista_ore) 
    #return lista_temp
    #return lista_indici




time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(hourly_trend_changes(time_series))
#print(time_series )


