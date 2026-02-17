# -----------------------------------------------------
import sys
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\first_week_project")
from src.data_loading import data_load
# -----------------------------------------------------

# ------------------------------------------------------------------
raw_data_path = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\first_week_project\data\raw_data\half_prepared_data.csv"
result = data_load(raw_data_path)
df = result.loadData()
#-----------------------------------------------------------------------------
print(df.sample(3))  