class CSVFile():
    def __init__(self, name):
        self.name=name
    
    #prendo la colonna quantita del file in formato float
    def get_data(self):
        my_file=open(self.name,'r')
        lista=[]
        #divido il csv in due colonne
        for linea in my_file:
            elementi = linea.split(',')
            elementi[-1]=elementi[-1].strip()
            if elementi[1] != 'Sales':
                lista.append(float(elementi[1]))
        my_file.close()
        return lista



class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')    

    def average(self, data): #creo la funzione media per far la media sui valori che mi servono (SUI DELTA)
        prev_value = None
        lista_delta=[]
        lista_elements=data
       
        for item in data:
            #all'inizio do il mio valore iniziale
            if prev_value is None:
                prev_value = item
                print('\t\t*prev_value: {}' .format(prev_value))
            #dal secondo valore in poi
            else:
                #calcolo la media
                delta = (item-prev_value)
                #prev_value mi diventa il valore di item così al prossimo ciclo sarà il valore precendete
                print('\t\t*il delta è {}' .format(delta))
                prev_value = item
                #popolo l'array coi valori(medie)
                lista_delta.append(delta)
            #sommo tutti i valori(medie) all'ultimo valore
                
        average = (sum(lista_delta)/len(lista_delta))
        print('\t*average in formula average: "{}"'.format(average))
        return average

    def evaluate(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel():
    def predict(self, data):
        prediction = []
        lista_value = data[-24:-12]
        last_value = lista_value[-1]
        print('\t*last value: "{}"'.format(last_value))

        model=Model()
        average = model.average(data) #faccio la media con la formula media
        print('\t*average in predict: "{}"'.format(average))
        prediction = average + float(last_value)
        return prediction

    def evaluate(self, data_prediction, data_real):
        delta = []
        import math
        for i in len(data_prediction):
            delta[i]=math.abs(data_prediction[i]-data_real[i])
        model=Model()
        average = model.average(delta)
        return delta

class FitIncrementModel (IncrementModel):
    
    def fit(self, dataset, datapredict):
        #self.global_avg_increment = None

        #prendo il dataset(lista_fit) come i 24 mesi prima della mia predizione
        
        for item in datapredict:
            
            model = Model()
            average_dataset = model.average(dataset)
            print('\t**la media del dataset è: "{}"'.format(average_dataset))
            average_predict = model.average(datapredict)
            print('\t**la media del predict è: "{}"'.format(average_predict))
    
            lista_av_fit_e_predict = [average_dataset, average_predict]
            print('\t*la lista media fit e predict è: "{}"' .format(lista_av_fit_e_predict))
                
            fit_prediction = ((average_dataset+average_predict)/2)+datapredict[-1]
        return fit_prediction
        

#--- CORPO DEL PROGRAMMA ---
shampoo=CSVFile(name='shampoo_sales.csv')
lista_shampoo=shampoo.get_data()
print('*{}'.format(lista_shampoo))

#creo le liste fit e predict 
lista_fit=[]
lista_predict=[]
for i in range(-1,-12):
    lista_predict=lista_shampoo[i]
for i in range(0,24):
    lista_fit=lista_shampoo[i]

increment_model=IncrementModel()
prediction_value=increment_model.predict(lista_shampoo)
print('la predizione incr_mod è: "{}"'.format(prediction_value))
increment_model.evaluate(prediction_value,lista_predict)

    

#