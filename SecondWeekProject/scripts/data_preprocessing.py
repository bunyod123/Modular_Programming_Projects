import sys,os
import pandas as pd
sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\SecondWeekProject")

# logger ni qoshamiz
from src.logger import get_logger
logger = get_logger("data_preprocessing")


data_link = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\SecondWeekProject\data\raw_data\train.csv"
df = pd.read_csv(data_link)

from src.data_preprocessing import Preprocessing
step = Preprocessing(df)

df1 = step.fillingNan().logTransformation().scaling().getDataset()

print(df1.head())

# Datani saqlash
try:
    folder = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\SecondWeekProject\data\preprocessed_data"    
    path = os.path.join(folder, "preprocessed_data.csv")
    df1.to_csv(path, index = False)
    logger.info("preprocessed data saqlandi")        
except Exception as e:
    logger.info("Datani saqlashda xatolik boldi")
        
    