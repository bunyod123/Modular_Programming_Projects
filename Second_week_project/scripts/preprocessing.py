import sys
import pandas as pd
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\second_week_project")

# Class va data ni import qilish
from source.preprocessing import Prerocessing
df = pd.read_csv(r"")

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
