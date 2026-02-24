import sys
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\Second_week_project")
df = pd.read_csv(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\first_week_project\data_sampling\over_sampled_final_data.csv")

from source.model_training import ModelTraining


X = df.drop("Score_class", axis=1, errors='ignore')
y = df["Score_class"]

result = ModelTraining(X=X,y=y)

jadval = result.train_all_models()

print(jadval)



eng_zor_model_nomi = jadval.iloc[0]["Model"]
eng_zor_natija = jadval.iloc[0]["accuracy"]

eng_yomon_model_nomi = jadval.iloc[-1]["Model"]
eng_yomon_natija = jadval.iloc[-1]["accuracy"]

print(f"Eng zo'r model: {eng_yomon_model_nomi} (accuracy: {eng_yomon_natija})")
print(f"Eng zo'r model: {eng_yomon_model_nomi} (accuracy: {eng_yomon_natija})")


best_model_object = result.trained_models[eng_zor_model_nomi]
bad_model_object = result.trained_models[eng_yomon_model_nomi]

# 4. Modelni faylga saqlash
fayl_nomi = "best_model.pkl"
joblib.dump(best_model_object, fayl_nomi)

fayl_nomi = "bad_model.pkl"
joblib.dump(bad_model_object, fayl_nomi)

