import sys
import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject")
df = pd.read_csv(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject\data\sampled_data\sampled_data.csv")


from src.model_trainig import ModelTraining


X = df.drop(columns=['Range_km_level','Price_level'])
y = df[['Range_km_level','Price_level']]

result = ModelTraining(X=X,y=y)

jadval = result.train_all_models()

print(jadval)


eng_zor_model = jadval.iloc[0]["Model"]
eng_zor_natija = jadval.iloc[0]["Accuracy"]

eng_yomon_model = jadval.iloc[-1]["Model"]
eng_yomon_natija = jadval.iloc[-1]["Accuracy"]

print(f"Eng zo'r model: {eng_zor_model} (Accuracy: {eng_zor_natija})")
print(f"Eng yomon model: {eng_yomon_model} (Accuracy: {eng_yomon_natija})")


best_model_object = result.trained_models[eng_zor_model]
bad_model_object = result.trained_models[eng_yomon_model]

# 4. Modelni faylga saqlash
path = r"C:\Users\bunyo\onedrive\desktop\AI_Course\ModularProgramProjects\finalProject\model\best_model"
full_path = os.path.join(path,"best_model.pkl")
joblib.dump(best_model_object, full_path)


bad_model_path = r"C:\Users\bunyo\onedrive\desktop\AI_Course\ModularProgramProjects\finalProject\model\bad_model"
bad_full_path = os.path.join(bad_model_path,"bad_model.pkl")
joblib.dump(bad_model_object, bad_full_path)

