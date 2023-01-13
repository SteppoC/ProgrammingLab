class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementalModel():
    def predict(self, data):
        prev_value = None
        differenza_valori = []
    for item in data:
        if prev_value is None:
            prev_value = item
        else:
            value = (item-prev_value)/2
            prev_value = item
            differenza_valori.append(value)
            prediction = (sum(differenza_valori))+item
    return prediction


mia_lista = [1,5,9]

incremental_model = IncrementalModel()
prediction_value = incremental_model.prediction(mia_lista)
print(prediction_value)
