import sys
import pandas as pd
sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\FourthWeekProject")

# Class va data ni import qilish
from src.data_preprocessing import Prerocessing
from scripts.feature_engineering import engineered_data
df = engineered_data

# ----------------------------------------------------------------------------
# data uchun ordinal encoding yaratish
mapping = {
    'diet_quality': ['Poor', 'Fair', 'Good'],
    'parental_education_level': ['High School', 'Bachelor', 'Master'],
    'internet_quality': ['Poor', 'Average', 'Good']
    }

# ----------------------------------------------------------------------------
# class orqali preprocessing qilish
result = Prerocessing(df=df)

pre_data = (
    result.Nan_toldiruvchi()
    .ordinal_encoder(mapping=mapping)
    .Encoder()
    .scaling(target = 'exam_score')
    .get_preprocessed_data()
)
print(pre_data.head())

# ----------------------------------------------------------------------
# Class orqali preprocessed_data ni saqlash
result.data_save()
