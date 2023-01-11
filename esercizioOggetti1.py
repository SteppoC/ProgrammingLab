class CSVFile():
    #inizializzo l'oggetto sul nome del file
    def __init__(self,name):
        self.name=name
        
    #creo l'attributo name che contiene il nome del 
    def get_data(self):
        my_file=open(self.name,'r')
        lista=[]
        
        for linea in my_file:
            elementi=linea.split(',')

            elementi[-1]=elementi[-1].strip() #formula magica per eliminare \n
            
            if elementi[0]!='Date':
                lista.append(elementi)
        return lista

shampoo = CSVFile('shampoo_sales.csv')
print(shampoo.get_data())