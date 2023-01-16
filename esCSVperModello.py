class CSVFile():
    def __init__(self,name):
        self.name=name
        if type(name) is not str:
            raise Exception('*il nome del file non è una stringa!')

    #prendo il file, lo apro, leggo i dati e prendo solo i valori
    def get_data(self,start=None, end=None):
        file_leggibile=True

        #apro il file se leggibile
        try:
            my_file=open(self.name,'r')
        except:
            print('Errore: non riesco a leggere il file')
            file_leggibile=False
            
        #prendo solo i valori numerici del file
        if file_leggibile:
            lista=[]
            
            for i,linea in enumerate(my_file):
                if i>=start and i<=end:
                    elementi=linea.split(',')
                    #qui elimino \n
                    elementi[-1]=elementi[-1].strip()
                    #ritorno la lista degli elementi selezionati
                    lista.append(elementi)
        return lista

class NumericalCSVFile(CSVFile):
    def get_data():
        #prendo la get data e la trasformo in valore numerico
        string_data = super().get_data()
        numerical_lista = []
        #ciclo sulle righe del file originale
        for linee_string in string_data:
            #numerical_riga = []
            for i,elemento in enumerate(linee_string):
                try:
                    numerical_lista.append(float(elemento))
                except Exception as e:
                    print('non riesco a convertire il valore')
                    break
            return numerical_lista        

test = CSVFile('test.csv')
print(test.get_data(1,3))

test_num = NumericalCSVFile('test.csv')
print(test_num.get_data(1,3))