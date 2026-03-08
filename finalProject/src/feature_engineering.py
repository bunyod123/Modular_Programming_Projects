import sys
from pathlib import Path
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject")
from src.log import get_logger
logging = get_logger('feature_engineering')



def feature_engineering(df):
    try:
        logging.info("Feature engineering started")
        
        df = df.drop(columns=['Name'])
        logging.info("Name columns is dropped")
        
        df['FastCharge_time_hrs'] = df['Battery_kWh	'] / df['Fast_charger(kW)']
        logging.info('Fast charge hours columns is added')
        
        df['Energy_weight_ratio'] = df['Battery_kwh'] / df['Weight_kg']
        logging.info('Energy weight ratio columns is created')
        
        df['Added_Range_1Stop'] = df['Firth_stop_range_km'] - df['Range_km']
        logging.info(f"Range first stop column is added")
        
        return df
    except Exception as e:
        print(f"there is an error: {e}")
        
        
def data_save(df2):
    try:
        current_file = Path(__file__).resolve()
        project_folder = current_file.parent.parent

        data_path = project_folder/"data"/"engineered_data"
        data_path.mkdir(parents=True, exist_ok=True)
        
        full_data_path = data_path/"engineered_data.csv"
        df2.to_csv(full_data_path, index = False)
        logging.info(f"Engineered data is saved with {df2.shape}")
        return True

    except Exception as e:
        logging.info(f"Errors while data saving {e}")
