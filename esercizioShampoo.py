#definisco la funzione somma
def sum_csv(file_name):
    #pass
   
#apro il file csv
    my_file=open(file_name,'r')
#print(my_file.read()[0:10])→lo carica e lo legge

    #creo la variabile fuori della somma
    listaQuantita=[]

    #per ogni riga divido le singole righe in data e quantità in base alla virgola
    for line in my_file:
        riga=line.split(',')
        if riga[0]!='Date':
            data=riga[0]
            quantita=riga[1]
        #trasformo in numero la stringa della quantità, che non è un numero e lo aggiungo alla lista che era vuota
            listaQuantita.append(float(quantita))
        #sommo le singole quantità
            #sommaQuantita+=quantita
    my_file.close()
    
    #sommo le quantità dentro la listaQuantita
    #totale=0
    #for somma in listaQuantita:
    #    totale+=somma
    #return totale
    totale = sum(listaQuantita)
    return totale

print(sum_csv('shampoo_sales.csv'))