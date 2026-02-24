# -----------------------------------------------------
import sys
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\Second_week_project")
from source.data_loading import data_loading
# -----------------------------------------------------

# ------------------------------------------------------------------
raw_data_path = r"C:\Users\bunyo\onedrive\desktop\AI_Course\ModularProgramProjects\Second_week_project\data\scrapped_data\earthquake.csv"
result = data_loading(raw_data_path)
df = result.load_data()
#-----------------------------------------------------------------------------
print(df.sample(3))  