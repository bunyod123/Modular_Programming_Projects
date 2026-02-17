import pandas as pd
import numpy as np
import sys
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer

sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\FourthWeekProject")
from src.log import get_logger
logging = get_logger("auto_pipline")

class Pipeline(BaseEstimator):   
    

    def __init__(self, df, target, model=None):
        self.df = df.copy()
        self.target = target
        self.model_algorithm = model
        self.model = None
        self.preprocessor = None
    

    def prepare_feature(self):
        X = self.df.drop(columns=[self.target])
        y = self.df[self.target]
        logging.log("X va y fetures tayinlandi")
        
        num_col = X.select_dtypes(include=[np.number]).columns.tolist()
        cat_col = X.select_dtypes(exclude=[np.number]).columns.tolist()

    
        numeric_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', MinMaxScaler())
        ])
        logging.info("Numerical nan qiymatlar toldirildi")
        
        categorical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1))
        ])
        logging.info("Categorical nan qiymatlar toldirildi")
        
        self.preprocessor = ColumnTransformer([
            ('num', numeric_pipeline, num_col),
            ('cat', categorical_pipeline, cat_col)
        ])

        return X, y

    def fitting(self):
        X, y = self.prepare_feature()

        if self.model_algorithm is None:
            raise ValueError("No model specified. Pass a scikit-learn estimator.")

        
        self.model = Pipeline([
            ('preprocessor', self.preprocessor),
            ('estimator', self.model_algorithm)
        ])
        logging.info("Modelga data fit qilindi")
        
        self.model.fit(X, y)
        return self

    def predict(self, X=None):
        if self.model is None:
            raise ValueError("Model not fitted yet. Call fit() first.")
        if X is None:
            X = self.df.drop(columns=[self.target])
        logging.info("model predict qilish boshlandi")
        return self.model.predict(X)

    def score(self, X=None, y=None):
        if self.model is None:
            raise ValueError("Model not fitted yet. Call fit() first.")
        if X is None and y is None:
            X = self.df.drop(columns=[self.target])
            y = self.df[self.target]
        logging.info("Modelni predict scori olchandi")
        return self.model.score(X, y)
