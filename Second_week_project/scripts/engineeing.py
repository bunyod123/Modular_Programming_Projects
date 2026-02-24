import pandas as pd
import sys
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\Second_week_project")

from source.engineering import feature_engineering, data_save
from scripts.data_loading import df

if df is not None:
    engineered_data = feature_engineering(df=df)

    data_save(df=engineered_data)
    
else:
    print("Dataset topilmadi")

print(engineered_data)


