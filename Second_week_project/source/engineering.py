import pandas as pd
import sys
from pathlib import Path
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\Second_week_project")

# ---------------------------------------------------------------------------------------------

# kerakli datani chaqrish
from source.log import get_logger
# from scripts.data_loading import df

logging = get_logger("feature_engineering")

# --------------------------------------------------------------------------------------------

# Feature engineering
def feature_engineering(df):
    try:
        logging.info("Feature engineering boshlandi")
        
        df = df.drop(['Location','Date','Network'], axis=1)
        logging.info('Location va Date va Network ustuni tashab yuborildi')
        
        df['Is_Shallow'] = (df['Depth'] < 70).astype(int)
        logging.info("Zilzila chuqurligi asosida chuqur yoki sayoz ligi qoshildi")
        
        
        df['Mag_Level'] = pd.cut(df['Magnituda'], bins=[0, 3, 5, 8], labels=['safe', 'dangerous', 'very deangerous'])  
        logging.info('global connectivity qoshildi')
        
        df2 = df.dropna()
        logging.info("Magnituda ustunida nan qiymati bor 79 ta qator tashlab yuborildi")
        return df
        
    except Exception as e:
        logging.info(f"Feature engineering qilishda xatolik boldi {e}")
        
        
        
# ---------------------------------------------------------------------------------------------

# Engineered datani saqlash
def data_save(df2):
    try:
        current_file = Path(__file__).resolve()
        project_folder = current_file.parent.parent

        data_path = project_folder/"data"/"engineered_data"
        data_path.mkdir(parents=True, exist_ok=True)
        
        full_data_path = data_path/"engineered_data.csv"
        df2.to_csv(full_data_path, index = False)
        logging.info(f"Engineered data saqlandi {df2.shape}")
        return True

    except Exception as e:
        logging.info(f"Datasetni saqlashda xatolik boldi {e}")