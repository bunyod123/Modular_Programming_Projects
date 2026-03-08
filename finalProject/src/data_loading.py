import pandas as pd
import sys
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject")

from src.log import get_logger
logging = get_logger('data_loading')

class data_load:
    logging.info('Data_set loading is started')
    def __init__(self, path:str, num:int):
        self.path = path
        self.num = 4
    
   
    def load_data(self):
        try:
            df = pd.read_csv(self.path)
            logging.info(f"data_set loaded with {df.shape[0]} rows and {df.shape[1]} columns")
            return self.df.sample(self.num)
    
        except Exception as e:
            print(f'data_set not loaded {e}')
