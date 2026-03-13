import sys
import pandas as pd
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\FinalProject")

# Class va data ni import qilish
from src.data_preprocessor import Preprocesor
df = pd.read_csv(r"C:\Users\bunyo\onedrive\desktop\AI_Course\ModularProgramProjects\FinalProject\data\engineered_data\engineered_data.csv")


# ----------------------------------------------------------------------------
# ordinal encoding yaratish
mapping = {
    'Price_level' : ['cheap','affordable','expensive'],
    'Range_km_level' : ['short','middle','long']
           }

target = ['Price_level','Range_km_level']
# ----------------------------------------------------------------------------

# class orqali preprocessing qilish
result = Preprocesor(df=df)

pre_data = (
    result.fill_nan()
    .ordinal_encoding(mapping=mapping)
    .scaler(target = target)
    .get_preprocessed_data()
)
print(pre_data.head())

# ----------------------------------------------------------------------
# Class orqali preprocessed_data ni saqlash
result.data_save()
