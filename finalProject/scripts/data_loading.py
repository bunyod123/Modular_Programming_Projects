import sys
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject")

from src.data_loading import data_load
path = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject\data\scraped_raw_data\car_data.csv"

result = data_load(path=path, num=4)
result.load_data()