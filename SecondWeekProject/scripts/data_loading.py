# kerakli kutubxona
import sys

# src file linkini olish
sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\SecondWeekProject")
from src.data_loading import data_load

# ------------------------------------------------------------------------------------------------------

# data ni yuklash
data_link = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\SecondWeekProject\data\raw_data\train.csv"
loading = data_load(data_link)
df = loading.load()

# -------------------------------------------------------------------------------------------------

print(df.head())