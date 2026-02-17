import sys
import joblib
from sklearn.model_selection import train_test_split

sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\FourthWeekProject")

from src.model_training import ModelTraining
from scripts.data_preprocessing import pre_data

X = pre_data.drop("exam_score", axis=1, errors='ignore')
y = pre_data["exam_score"]

result = ModelTraining(X=X,y=y)

jadval = result.train_all_models()

print(jadval)



eng_zor_model_nomi = jadval.iloc[0]["Model"]
eng_zor_natija = jadval.iloc[0]["Test R2"]

eng_yomon_model_nomi = jadval.iloc[-1]["Model"]
eng_yomon_natija = jadval.iloc[-1]["Test R2"]

print(f"Eng zo'r model: {eng_yomon_model_nomi} (R2: {eng_yomon_natija})")
print(f"Eng zo'r model: {eng_yomon_model_nomi} (R2: {eng_yomon_natija})")


best_model_object = result.trained_models[eng_zor_model_nomi]
bad_model_object = result.trained_models[eng_yomon_model_nomi]

# 4. Modelni faylga saqlaymiz
fayl_nomi = "best_model.pkl"
joblib.dump(best_model_object, fayl_nomi)

fayl_nomi = "bad_model.pkl"
joblib.dump(bad_model_object, fayl_nomi)

