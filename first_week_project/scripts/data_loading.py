# -----------------------------------------------------
import sys
sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\FourthWeekProject")
from src.data_loading import data_load
# -----------------------------------------------------

# ------------------------------------------------------------------
raw_data_path = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\FourthWeekProject\data\raw_data\student_habits_performance.csv"
result = data_load(raw_data_path)
df = result.loadData()
#-----------------------------------------------------------------------------
print(df.sample(3))