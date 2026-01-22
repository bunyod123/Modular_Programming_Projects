import pandas as pd

class DataLoad:
    
    def __init__(self, x):
        self.x = x
    

    def data_loader(self):
        result = pd.read_csv(self.x)
        return result
    