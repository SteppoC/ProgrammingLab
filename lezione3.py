print('---ECCEZIONI---')
my_var='ciao'
try:
    my_var=float(my_var)
except:
    print('no! my_var non è un numero ma è:  {}' .format(my_var))    
    my_var=0.0
    print('uso {} come valore di my_var'.format(my_var))
print('-------------')
my_var='cane'
try:
    my_var=float(my_var)
except Exception as e:
    print('no! my_var non è un numero ma è:  {}' .format(my_var))
    print('ho avuto l\'errore: "{}"'.format(e))
    #'e' mi riporta l'errore che mi darebbe pyhton
    
print('-------')

my_var='cane'
try:
    my_var=float(my_var)
except ValueError:
    print('non è valor numerico')
except TypeError:
    print('ho havuto errore di tipo')
except Exception as e:
    print('l\'errore è: {}' .format(e))
#funziona a cascata tipo gli if: alla fine se non trovo l'errore che pensavo stampo l'errore di python

print('--------------')
print('-ESERCIZIO -a-')
print('--------------')

class CSVFile():
    #inizializzo l'oggetto sul nome del file
    def __init__(self,name):
        self.name=name
        
    #creo l'attributo name che contiene il nome del 
    def get_data(self):
        
        ####qui inserisco il controllo se il file esiste
        file_leggibile=True 
        try:
            my_file=open(self.name,'r')
        except:
            print('Errore: non riesco a leggere il file')
            file_leggibile=False
        
        if file_leggibile:   #se trovo il file ed è leggibile fa  tutto come nell'esercizio prima 
            lista=[]
        
            for linea in my_file:
                elementi=linea.split(',')
    
                elementi[-1]=elementi[-1].strip() #formula magica per eliminare \n
                
                if elementi[0]!='Date':
                    lista.append(elementi)
            return lista

shampoo = CSVFile('shampoo_sales.csv')
print(shampoo.get_data())

print('--------------')
print('-ESERCIZIO -b-')
print('--------------')

class NumericalCSVFile():
    #inizializzo l'oggetto sul nome del file
    def __init__(self,name):
        self.name=name
        
    #creo l'attributo name che contiene il nome del 
    def get_data(self):
        
        ####qui inserisco il controllo se il file esiste
        file_leggibile=True 
        try:
            my_file=open(self.name,'r')
        except:
            print('Errore: non riesco a leggere il file')
            file_leggibile=False
        
        if file_leggibile:   #se trovo il file ed è leggibile fa  tutto come nell'esercizio prima 
            lista=[]
        
            for i,linea in enumerate(my_file): #metto un contatore per stampare poi la riga d'errore
                elementi=linea.split(',')
    
                elementi[-1]=elementi[-1].strip() #formula magica per eliminare \n
                
                if elementi[0]!='Date':
                    try:
                        elementi_numero=float(elementi[1])
                        lista.append(elementi)
                    except Exception as errore:
                        print('*Errore: alla riga "{}"'.format(i+1))
                        print('*Errore: non posso convertire perchè ci sono valori "{}"'.format(type(elementi)))
                        print('*l\'Errore genetato è "{}"' .format(errore))
            return lista

shampoo = NumericalCSVFile('shampoo_sales.csv')
print(shampoo.get_data())