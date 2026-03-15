import sys
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler,OrdinalEncoder,LabelEncoder
from sklearn.impute import SimpleImputer

sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject")
from src.log import get_logger
logging = get_logger('preprocessing')


class Preprocesor:
    def __init__(self, df):
        self.min_max_scaler = MinMaxScaler()
        self.labeling = LabelEncoder()
        self.df = df
        self.cat_cols = self.df.select_dtypes(exclude=[np.number]).columns.tolist()
        self.num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        logging.info("Data preprocessing is started")   
    
    
    def fill_nan(self):
        try:
            if self.num_cols:
                num_col_imputer = SimpleImputer(strategy='mean')
                self.df[self.num_cols] = num_col_imputer.fit_transform(self.df[self.num_cols])
                logging.info(f"{self.num_cols} columns filled with mean value of them")
                
            if self.cat_cols:
                cat_cols_imputer = SimpleImputer(strategy='most_frequent')
                self.df[self.cat_cols] = cat_cols_imputer.fit_transform(self.df[self.cat_cols])
                logging.info(f"{self.cat_cols} columns filled with most frequent values of them")
            return self
        
        except Exception as e:
            print(f"There is problem with NaN value filling {e}")
        
        
    def ordinal_encoding(self, mapping):
        try:
            for column, order in mapping.items():
                if column in self.df.columns:
                    encoder = OrdinalEncoder(
                        categories=[order],
                        handle_unknown='use_encoded_value',
                        unknown_value=-2,
                        dtype=int
                    )
                    self.df[[column]] = encoder.fit_transform(self.df[[column]]) + 1
                    logging.info(f"{column} features are encoded with Ordinal Encoder")
            return self            
        
        except Exception as e:
            logging.error(f"Erors: {e}")
    
    def label_encoder(self):
        if self.cat_cols:
            try:
                for col in self.cat_cols:
                    if self.df[col].nunique() < 4:
                        dum = pd.get_dummies(self.df[col], prefix=col, dtype=int)
                        self.df = self.df.drop(columns=[col])
                        self.df = pd.concat([self.df, dum], axis=1)
                        logging.info(f"{col} fetures are encoded with one-hot-encoding")
                    else:
                        self.df[col] = self.labeling.fit_transform(self.df[col]) # type: ignore
                        logging.info(f"{col} features encoded with label encoder")                                          

            except Exception as e:
                logging.info("There is an error: {e}")
        return self
    
    
    def scaler(self, target):
        num_col = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        try:            
            if isinstance(target, str):
                target = [target]           
                num_col = [col for col in num_col if col not in target]
                
            if num_col:
                for col in num_col:
                    self.df[[col]] = self.min_max_scaler.fit_transform(self.df[[col]]) # type: ignore
                    logging.info(f"{col} features scaled with min_max scaler")
            return self
        
        except Exception as e:
            logging.info(f"there is error: {e}")
        
    
    def get_preprocessed_data(self):
        try:
            logging.info("Data preprocessing is finishid succesfully")
            return self.df
        except Exception as e:
            logging.info(f"Errors: {e}")
            
            
    def data_save(self):
        try:
            current_file = Path(__file__).resolve()
            project_folder = current_file.parent.parent

            data_path = project_folder/"data"/"preprocessed_data"
            data_path.mkdir(parents=True, exist_ok=True)
            full_data_path = data_path/"preprocessed_data.csv"
            self.df.to_csv(full_data_path, index = False)
            logging.info(f"Preprocessed data is saved with {self.df.shape[0]} rows  {self.df.shape[1]} columns")

        except Exception as e:
            logging.info(f"Error: {e}")
            