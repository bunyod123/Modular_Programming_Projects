
import pandas as pd
import sys

# ------------------------------------------------------------------------------------
# Logging uchun path 
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\first_week_project")
from src.log import get_logger
loging = get_logger('data_loading')
loging.info("Data setni yuklash boshlandi")

# ----------------------------------------------------------------------------------------
# Data loading uchun class
class data_load:
    def __init__(self, path: str):
        self.path = path
        
    def loadData(self):
        try:
            df = pd.read_csv(self.path)
            loging.info(f"Dataset yuklandi {df.shape[0]} ta qator va {df.shape[1]} ta ustun bilan")
            return df
        except Exception as e:
            loging.info(f"Data set yuklanmadi {e}")
            
# ----------------------------------------------------------------------------------------
            
            
        