class CSVFile():
    #inizializzo l'oggetto sul nome del file
    def __init__(self,name):
        self.name=name
        if type(name) is not str:
            raise Exception('*il nome del file non è una stringa!')
            
    def get_data(self, start=None, end=None):
        
        ####qui inserisco il controllo se il file esiste
        file_leggibile=True 
        try:
            my_file=open(self.name,'r')
        except:
            print('Errore: non riesco a leggere il file')
            file_leggibile=False

        if start>=end:
            print('forse intendevi l\'ordine inverso... ed è quello che farò')
            new_start = end
            end = start
            start = new_start
            #raise Exception('*Errore: start "{}" è >= a end"{}"'.format(start,end))
        
        if file_leggibile:   #se trovo il file ed è leggibile fa  tutto come nell'esercizio prima 
            lista=[]
            start=start-1
            end=end-1
            for i,linea in enumerate(my_file):
                if i>=start and i<=end:
                    elementi=linea.split(',')
                    elementi[-1]=elementi[-1].strip() #formula magica per eliminare \n
                    #if elementi[0]!='Date':
                    lista.append(elementi)
            return lista

shampoo = CSVFile('shampoo_sales.csv')
print(shampoo.get_data(4,1))