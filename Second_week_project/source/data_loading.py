import sys
import pandas as pd

sys.path.append(r"C:\Users\bunyo\onedrive\desktop\AI_Course\ModularProgramProjects\Second_week_project")
from source import get_logger
logging = get_logger('data_loading')


class data_loading:
    
    def __init__(self, path:str):
        self.path = path
    logging.info("Datasetni yuklash boshlandi")    
    
    def load_data(self):
        try:
            data = pd.read_csv(self.path)
            logging.info(f"dataset yuklandi {data.shape[0]} ta qator va {data.shape[1]} ta ustun bilan")
            return data
        except Exception as e:
            logging.error("Data yuklashda xatolik boldi {e}")
            return None
        