
#======================
# Classe per file CSV
#======================

class CSVTimeSeriesFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name


    def get_data(self):

        # Inizializzo una lista vuota per salvare i valori
        temperature= []
        
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            
            # Esco dalla funzione tornando "niente".
            return None
        
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
           
  ''' 
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(' ')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'epoche':
                   
                # Setto la data ed il valore
                epoche  = elements[0]
                temp    = elements[1]
                 
                # La variabile "temp" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    temp = float(temp)
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                
                # Infine aggiungo alla lista dei valori questo valore
                #append puo passare solo 1 dato
                temperature.append(epoche,temp)
  '''
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return temperature
    
       

#======================
# Corpo del programma
#======================

#def  hourly_trend_changes(time_series ):
    #inizializzo un vettore vuoto
    #variazioni=[]


   # return variazioni()


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(time_series )
