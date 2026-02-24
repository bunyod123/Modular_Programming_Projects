import sys
import pandas as pd
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\second_week_project")

# Class va data ni import qilish
from source.prerocessing import Prerocessing
df = pd.read_csv(r"C:\Users\bunyo\onedrive\desktop\AI_Course\ModularProgramProjects\Second_week_project\data\engineered_data\engineered_data.csv")


# ----------------------------------------------------------------------------
# data uchun ordinal encoding yaratish
mapping = {
    'Level': ['safe','dangerous','very deangerous']
    }

# ----------------------------------------------------------------------------
# class orqali preprocessing qilish
result = Prerocessing(df=df)

pre_data = (
    result.Nan_toldiruvchi()
    .ordinal_encoder(mapping=mapping)
    .Encoder()
    .scaling(target = 'Mag_Level')
    .get_preprocessed_data()
)
print(pre_data.head())

# ----------------------------------------------------------------------
# Class orqali preprocessed_data ni saqlash
result.data_save()
