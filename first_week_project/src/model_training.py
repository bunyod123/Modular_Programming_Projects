import sys
sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\FourthWeekProject")
from src.log import get_logger
logging = get_logger('model_training')


import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import r2_score, mean_absolute_error


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.linear_model import Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor



class ModelTraining:
    def __init__(self, X, y, k_folds=6):
        self.X = X
        self.y = y
        self.k_folds = k_folds
        
        # O'qitilgan modellarni saqlash uchun lug'at
        self.trained_models = {} 
        
        self.models = {
                "Linear Regression": LinearRegression(),
                "Ridge": Ridge(alpha=1.0),
                "Lasso": Lasso(alpha=0.1),
                "Decision Tree": DecisionTreeRegressor(), 
                "Random Forest": RandomForestRegressor(random_state=18),
                "XGBoost": XGBRegressor(random_state=37),
                "KNN": KNeighborsRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(random_state=77)
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
                cv_scores = cross_val_score(model, X_train, y_train, cv=kf, scoring='r2')
                avg_cv_r2 = cv_scores.mean()

                # training setda o'qitish
                model.fit(X_train, y_train)
                
                # modelni saqlab qo'yish
                self.trained_models[name] = model 

                # Test setda tekshirish
                preds = model.predict(X_test)
                r2 = r2_score(y_test, preds)
                mae = mean_absolute_error(y_test, preds)

                results.append({
                    "Model": name,
                    "CV R2 (avg)": round(avg_cv_r2, 2),
                    "Test R2": round(r2, 2),
                    "Test MAE": round(mae, 2)
                })

            return pd.DataFrame(results).sort_values(by="Test R2", ascending=False)

        except Exception as e:
            logging.error(f"Xatolik: {e}")
            raise e