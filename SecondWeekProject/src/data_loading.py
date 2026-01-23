# -----------------------------------------------------------------------------------
import pandas as pd
import sys

#-----------------------------------------------------------------------------------------

sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\SecondWeekProject")
from src.logger import get_logger
logger = get_logger("data_loading")

logger.info("Data yuklash boshqlandi.")


#------------------------------------------------------------------------------------------

# data koad uchun class yaratamiz
class data_load:
    def __init__(self, path : str):
        self.path = path

    def load(self):
        try:
            df = pd.read_csv(self.path)
            logger.info("Dataset yuklandi")
            return df
        except Exception as e:
            logger.info(f"Data yuklanmadi {e}")
            
# ------------------------------------------------------------------------------------------