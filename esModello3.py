#secondo sarusso
class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

    def evaluate(self, data):
        errors = []
        for window_offset in range(len(data)-self.window_length):
            evaluation_window_data=data[window_offset:window_offset+self.window_length]
            predicted = self.predict(evaluation_window_data)
            actual = data[self.window_length+window_offset]
            errors.append(abs(actual-predicted))

        return sum(errors)/float(len(errors))

class IncrementModel(Model):
    def __init__(self, window_length=None):
        self.window_length = window_length

    def compute_avg_increment(self, data):
        prev_item = None
        increments = []
        for item in data:
            if prev_item is None:
                prev_item=item
            else:
                increments.append(item-prev_item)
        return sum(increments)/float(len(increments))

    def predict(self, data):
        window_avg_increment = self.compute_avg_increment(data)
        return data[-1]+window_avg_increment

class FitIncrementModel(IncrementModel):
    def fit(self, data):
        self.global_avg_increment=self.compute_avg_increment(data)

    def predict(self, data):
        window_avg_increment = self.compute_avg_increment(data)
        return data[-1] + (self.global_avg_increment + window_avg_increment)/2.0
        
        