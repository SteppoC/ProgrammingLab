class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel():
    def predict(self, data):
        #valore precedente per far la madia poi
        prev_value = None
        #creo un array per contenere i conti che andrò a fare
        lista_delta = []
        
        for item in data:
            #all'inizio do il mio valore iniziale
            if prev_value is None:
                prev_value = item
                print('\t*prev_value: {}' .format(prev_value))
            #dal secondo valore in poi
            else:
                #calcolo il delta
                delta = (item-prev_value)
                #prev_value mi diventa il valore di item così al prossimo ciclo sarà il valore precendete
                print('\t*il delta è {}' .format(delta))
                prev_value = item
                #popolo l'array coi valori(medie)
                lista_delta.append(delta)
            #calcolo la media e la sommo all'ultimo valore
            prediction = (sum(lista_delta)/len(lista_delta))+item
        return prediction

        
#--- provo ---
mia_lista = [50,52,60] #predizione con [50,52,60]=65
print(mia_lista)

increment_model = IncrementModel()
prediction_value = increment_model.predict(mia_lista)
print('la predizione è: {}' .format(prediction_value))
