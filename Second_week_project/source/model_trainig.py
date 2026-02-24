import sys
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\Second_week_project")
from source.log import get_logger
logging = get_logger('model_training')


import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import accuracy_score


from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier
# from sklearn.linear_model import Ridge, Lasso
from sklearn.neighbors import KNeighborsClassifier



class ModelTraining:
    def __init__(self, X, y, k_folds=6):
        self.X = X
        self.y = y
        self.k_folds = k_folds
        
        # modellarni saqlash uchun lug'at
        self.trained_models = {} 
        
        self.models = {
                "OvO": OneVsOneClassifier(LogisticRegression(max_iter=889,random_state=99)),
                "OvR": OneVsRestClassifier(LogisticRegression(max_iter=999,random_state=77)),
                "Decision Tree": DecisionTreeClassifier(), 
                "Random Forest": RandomForestClassifier(random_state=18),
                "XGBoost": XGBClassifier(random_state=37),
                "KNN": KNeighborsClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(random_state=77)
        }
      
      
        logging.info(f"Training boshlandi: X={X.shape}, y={y.shape}")

    def train_all_models(self):
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                self.X, self.y, test_size=0.18, random_state=69
            )

            kf = KFold(n_splits=self.k_folds, shuffle=True, random_state=39)
            results = []

            for name, model in self.models.items():
                logging.info(f"{name} o'qitilish boshlandi")

                # Cross Validation
                cv_scores = cross_val_score(model, X_train, y_train, cv=kf)
                avg_cv_ac = cv_scores.mean()

                
                model.fit(X_train, y_train)
                
                # modelni saqlash
                self.trained_models[name] = model 

               
                preds = model.predict(X_test)
                accuracy = accuracy_score(y_test,preds)


                results.append({
                    "Model": name,
                    "CV ACC (avg)": round(avg_cv_ac, 2),
                    "accuracy" : accuracy
                })

            return pd.DataFrame(results).sort_values(by="accuracy", ascending=False)

        except Exception as e:
            logging.error(f"Xatolik: {e}")