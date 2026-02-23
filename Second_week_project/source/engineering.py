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
        
        df = df.drop(['Location','Name'], axis=1)
        logging.info('Location va Universitet nomi ustuni tashab yuborildi')
        
        df['Total_Reputation'] = (df['Acedemik Reputation'] + df['employer_reputation']) / 2
        logging.info("Total ruputatsiya df ga qoshildi")
        
        
        df['Global_Connectivity'] = (df['international_faculty_ratio'] + df['international_research_network']) / 2  
        logging.info('global connectivity qoshildi')
        return df
        
    except Exception as e:
        logging.info(f"Feature engineering qilishda xatolik boldi {e}")
        
        
        
# ---------------------------------------------------------------------------------------------

# Engineered datani saqlash
def data_save(df):
    try:
        current_file = Path(__file__).resolve()
        project_folder = current_file.parent.parent

        data_path = project_folder/"data"/"engineered_data"
        data_path.mkdir(parents=True, exist_ok=True)
        
        full_data_path = data_path/"engineered_data.csv"
        df.to_csv(full_data_path, index = False)
        logging.info(f"Engineered data saqlandi {df.shape}")
        return True

    except Exception as e:
        logging.info(f"Datasetni saqlashda xatolik boldi {e}")