#apro e leggo il file linea per linea 
somma=0
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    #faccio lo split di ogni riga sulla virgola

    elementi=line.split(",")
    if(elementi[1]!='Sales\n'):
        valore=float(elementi[1])
        somma+=valore


print(somma)

