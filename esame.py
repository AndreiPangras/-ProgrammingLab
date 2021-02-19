
#======================
# Classe per file CSV
#======================
class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name


    def get_data(self):

        # Inizializzo una lista vuota per salvare i valori
        values = []

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto del'errore, 
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            
            # Esco dalla funzione tornando "niente".
            return None
        
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Setto la data ed il valore
                date  = elements[0]
                value = elements[1]
                
                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    value = float(value)
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                
                # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return values
    
        
#======================
# Corpo del programma
#======================

mio_file = CSVFile(name='shampoo_sales.csv')

print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))


class Model (object):
    def fit(self,data):
        pass

    def predict(self):
        pass

class IncrementoModel(Model):
    def fit(self,data):
        raise NotImplementedError('Questo modello non prevede un fit')

    def pedict(self,prev_mesi):
        #setto i numeri del mesi 
        n_mesi=len(prev_mesi)

        #creo una variabli per calcolarmi l'icremento medio
        icrement=0

        #processo i mesi nei queli devo fare i calcolarmi
        for i in rage(n_mesi):
           # Salto il primo mese in quanto non posso avere definito
            # un incremento se non ho almento due mesi
            if i == 0:
                continue
            else:
                # Calcolo l'incremento tra questo mese ed il precedente
                increments += prev_months[i] - prev_months[i-1]
                
        
        # Calcolo l'incremento medio divivendo la somam degli incrmenti sul totale dei mesi
        # ma meno uno: sopra ho scartato il primo mese in effetti!
        avg_increment = increments / (n_months-1)
        
        
     
        # Torno la predizione
        return prev_months[-1] + avg_increment


