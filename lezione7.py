print('------------------------')
print('- TEST PER IL CSV FILE -')
print('------------------------')

class CSVFile():
    #inizializzo l'oggetto sul nome del file
    def __init__(self,name):
        self.name=name
        if type(name) is not str:
            raise Exception('*il nome del file non è una stringa!')
            
    def get_data(self, start=None, end=None):
        ####qui inserisco il controllo se il file esiste
        file_leggibile=True
        #testing get_data    
        try:
            my_file=open(self.name,'r')
        except:
            print('#Errore: non riesco a leggere il file')
            file_leggibile=False

        #controllo che gli intervalli da leggere siano int
        #if type(start) or type(end) != int():
            #raise ('#Test get_data: gli intervalli non sono interi')

        #testo se c'è il file
        if my_file == None:
            raise ('#Test get_data: manca il file')

        if file_leggibile:   #se trovo il file ed è leggibile fa  tutto come nell'esercizio prima 
            lista=[]
            start=start-1
            end=end-1
            for i,linea in enumerate(my_file):
                if i>=start and i<=end:
                    elementi=linea.split(',')
                    elementi[-1]=elementi[-1].strip() #formula magica per eliminare \n
                    #if elementi[0]!='Date':
                        #testing se ha diviso secondo le virgole
                    controllo_virgola = ','
                    if controllo_virgola in elementi[0]:
                        raise('#Test get_data: gli elementi non sono stati divisi alla ","')   
                    elif controllo_virgola in elementi[1]:
                        raise('#Test get_data: gli elementi non sono stati divisi alla ","')
                    lista.append(elementi)
                    #controllo
                    if '-' not in elementi[0]:
                        raise('#Test get data: la data non è una data')
            return lista


        

shampoo = CSVFile('shampoo_sales.csv')
print(shampoo.get_data(1,4))


#if in elementi[0] == ',':
#    raise('#Test get_data: gli elementi non sono stati divisi alla ","')
#elif in elementi[1] == ',':
#    raise('#Test get_data: gli elementi non sono stati divisi alla ","')
