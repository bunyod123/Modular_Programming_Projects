import pandas as pd
import sys
from pathlib import Path
sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\FourthWeekProject")

# ---------------------------------------------------------------------------------------------

# kerakli datani chaqrish
from src.log import get_logger
# from scripts.data_loading import df

logging = get_logger("feature_engineering")

# --------------------------------------------------------------------------------------------

# Feature engineering funksiyasi
def feature_engineering(df):
    try:
        logging.info("Feature engineering boshlandi")
        
        df = df.drop("student_id",axis=1, errors='ignore' )
        logging.info("Student_Id ustuni tashlab yuborildi")
        
        df['total_screen_time'] = df['social_media_hours'] + df['netflix_hours']
        logging.info("Ijtimoiy tarmoqdan qancha foydalanish qoshildi")
        
        df['lifestyle_score'] = (df['sleep_hours'] + df['exercise_frequency'] + df['mental_health_rating'])/3
        logging.info("Faol hayot tarzi qoshildi")
        
        df['study_effectivness'] = (df['study_hours_per_day']) * (df['attendance_percentage']/100)
        logging.info("Qanchalik effective oqishi qoshildi")   
        
        return df
        
    except Exception as e:
        logging.info("Feature engineering qilishda xatolik boldi")
        
        
        
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
        logging.info("Datasetni saqlashda xatolik boldi")