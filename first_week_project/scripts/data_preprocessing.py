import sys
import pandas as pd
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\first_week_project")

# Class va data ni import qilish
from src.data_preprocessing import Prerocessing
from scripts.feature_engineering import engineered_data
df = engineered_data

# ----------------------------------------------------------------------------
# data uchun ordinal encoding yaratish
mapping = {
    'Score_class': ['Good','very good','great','really great','best',]
    }

# ----------------------------------------------------------------------------
# class orqali preprocessing qilish
result = Prerocessing(df=df)

pre_data = (
    result.Nan_toldiruvchi()
    .ordinal_encoder(mapping=mapping)
    .Encoder()
    .scaling(target = 'Score_class')
    .get_preprocessed_data()
)
print(pre_data.head())

# ----------------------------------------------------------------------
# Class orqali preprocessed_data ni saqlash
result.data_save()
