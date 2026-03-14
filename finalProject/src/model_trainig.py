# import sys
# sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject")
# from src.log import get_logger
# logging = get_logger('model_training')

# import pandas as pd
# from sklearn.model_selection import train_test_split, KFold, cross_val_score
# from sklearn.metrics import accuracy_score
# from sklearn.multioutput import MultiOutputClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC
# from xgboost import XGBClassifier

# class ModelTraining:
#     def __init__(self, X, y, k_folds=6):
#         self.X = X
#         self.y = y
#         self.k_folds = k_folds
        
#         self.trained_models = {} 
        
#         self.models = {
#             "Decision Tree": DecisionTreeClassifier(random_state=42),
#             "Random Forest": RandomForestClassifier(random_state=42),
#             "Extra Trees": ExtraTreesClassifier(random_state=42),
#             "KNN": KNeighborsClassifier(),
#             "Logistic Regression": MultiOutputClassifier(LogisticRegression(max_iter=1000, random_state=42)),
#             "SVM (SVC)": MultiOutputClassifier(SVC(random_state=42)),
#             "Gradient Boosting": MultiOutputClassifier(GradientBoostingClassifier(random_state=42)),
#             "XGBoost": MultiOutputClassifier(XGBClassifier(random_state=42, eval_metric='logloss'))
#         }
      
#         logging.info(f"Training boshlandi: X={X.shape}, y={y.shape}")

#     def train_all_models(self):
#         try:
#             X_train, X_test, y_train, y_test = train_test_split(
#                 self.X, self.y, test_size=0.18, random_state=69
#             )

#             kf = KFold(n_splits=self.k_folds, shuffle=True, random_state=39)
#             results = []

#             for name, model in self.models.items():
#                 logging.info(f"{name} o'qitilish boshlandi")

#                 cv_scores = cross_val_score(model, X_train, y_train, cv=kf)
#                 avg_cv_ac = cv_scores.mean()
                
#                 model.fit(X_train, y_train)
                
#                 self.trained_models[name] = model 
               
#                 preds = model.predict(X_test)
                
#                 accuracy = accuracy_score(y_test, preds)

#                 results.append({
#                     "Model": name,
#                     "CV ACC (avg)": round(avg_cv_ac, 4),
#                     "Accuracy": round(accuracy, 4)
#                 })
                
#                 logging.info(f"{name} muvaffaqiyatli o'qitildi. Accuracy: {accuracy:.4f}")

#             return pd.DataFrame(results).sort_values(by="Accuracy", ascending=False)

#         except Exception as e:
#             logging.error(f"Xatolik yuz berdi: {e}")
#             return None


import sys
# O'zingizning loyiha manzilingiz:
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject")
from src.log import get_logger
logging = get_logger('model_training')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import accuracy_score, make_scorer
from sklearn.multioutput import MultiOutputClassifier

# Modellar kutubxonalari
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier


def custom_multioutput_accuracy(y_true, y_pred):
    y_true_arr = np.array(y_true)
    y_pred_arr = np.array(y_pred)
    
    accuracies = []
    for i in range(y_true_arr.shape[1]):
        acc = accuracy_score(y_true_arr[:, i], y_pred_arr[:, i])
        accuracies.append(acc)
        
    return np.mean(accuracies)
# -----------------------------------------------------------------


class ModelTraining:
    def __init__(self, X, y, k_folds=6):
        self.X = X
        self.y = y
        self.k_folds = k_folds
        
        self.trained_models = {} 
        
        self.models = {
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "Random Forest": RandomForestClassifier(random_state=42),
            "Extra Trees": ExtraTreesClassifier(random_state=42),
            "KNN": KNeighborsClassifier(),
            "Logistic Regression": MultiOutputClassifier(LogisticRegression(max_iter=1000, random_state=42)),
            "SVM (SVC)": MultiOutputClassifier(SVC(random_state=42)),
            "Gradient Boosting": MultiOutputClassifier(GradientBoostingClassifier(random_state=42)),
            "XGBoost": MultiOutputClassifier(XGBClassifier(random_state=42, eval_metric='logloss'))
        }
      
        logging.info(f"Training boshlandi: X={X.shape}, y={y.shape}")

    def train_all_models(self):
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                self.X, self.y, test_size=0.18, random_state=69
            )

            kf = KFold(n_splits=self.k_folds, shuffle=True, random_state=39)
            results = []
            
            multi_scorer = make_scorer(custom_multioutput_accuracy)

            for name, model in self.models.items():
                logging.info(f"{name} o'qitilish boshlandi")

                cv_scores = cross_val_score(model, X_train, y_train, cv=kf, scoring=multi_scorer)
                avg_cv_ac = cv_scores.mean()
                
                model.fit(X_train, y_train)
                
                self.trained_models[name] = model 
               
                preds = model.predict(X_test)
                
                accuracy = custom_multioutput_accuracy(y_test, preds)

                results.append({
                    "Model": name,
                    "CV ACC (avg)": round(avg_cv_ac, 4),
                    "Accuracy": round(accuracy, 4)
                })
                
                logging.info(f"{name} muvaffaqiyatli o'qitildi. Accuracy: {accuracy:.4f}")

            return pd.DataFrame(results).sort_values(by="Accuracy", ascending=False)

        except Exception as e:
            logging.error(f"Xatolik yuz berdi: {e}")
            return None