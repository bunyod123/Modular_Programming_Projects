import pandas as pd
import numpy as np
import sys
import os
from pathlib import Path
from sklearn.preprocessing import LabelEncoder,MinMaxScaler,OrdinalEncoder
from sklearn.impute import SimpleImputer


# -------------------------------------------------------------------------------------------
# logging uchun path yaratish
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\first_week_project")
from src.log import get_logger
loging = get_logger("data_preprocessing")

# -------------------------------------------------------------------------------------------

# Class yaratish
class Prerocessing:
    def __init__(self, df):
        self.df = df.copy()
        self.labeling = LabelEncoder()
        self.minmax = MinMaxScaler()
        loging.info("Data preprocessing boshlandi")
        
# --------------------------------------------------------------------------------------- 
    
    # Nan qiymatlarni toldiruvchi funksiya      
    def Nan_toldiruvchi(self):
        try:
            num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            cat_cols = self.df.select_dtypes(exclude=[np.number]).columns.tolist()
            
            if num_cols:
                num_cols_imputer = SimpleImputer(strategy='mean')
                self.df[num_cols] = num_cols_imputer.fit_transform(self.df[num_cols])
                loging.info("Numerical qiymatlar toldirildi")
                
            if cat_cols:
                cat_cols_imputer = SimpleImputer(strategy='most_frequent')
                self.df[cat_cols] = cat_cols_imputer.fit_transform(self.df[cat_cols])
                loging.info("Categorical qiymat toldirildi")
        
            return self
        
        except Exception as e:
            loging.info(f"Xatolik yuz berdi {e}")
            
# ----------------------------------------------------------------------------------
    
    # ordinal bilan encoding qilish
    def ordinal_encoder(self, mapping):
        try:
            for column, order in mapping.items():
                if column in self.df.columns:
                    encoder = OrdinalEncoder(
                        categories=[order],
                        handle_unknown='use_encoded_value',
                        unknown_value=1
                    )
                    self.df[[column]] = encoder.fit_transform(self.df[[column]])
                    loging.info(f"ustun ordinal yordamida kodlandi.")
            return self
        except Exception as e:
            loging.error(f"Encodingda xatolik boldi: {e}")
            return self
         
# ----------------------------------------------------------------------------------   
       
    # Categorical qiymatlarni Encoding qilish funksiyasi       
    def Encoder(self):
        
        cat_colmns = self.df.select_dtypes(exclude = [np.number]).columns.tolist()
        
        if cat_colmns:
            try:
                for categ in cat_colmns:
                    if self.df[categ].nunique() < 3:
                        dums = pd.get_dummies(self.df[categ], prefix=categ, dtype=int)
                        self.df = self.df.drop(columns = [categ])
                        self.df = pd.concat([self.df, dums], axis=1)
                        loging.info("Ayrim ustunla One Hot bilan Encoding qilindi")
                    else:
                        self.df[categ] = self.labeling.fit_transform(self.df[categ])
                        loging.info("Ayrim ustunla Labeling bilan encoding qilindi")
                    
            except Exception as e:
                loging.info(f"Qandaydir xatolik boldi {e}")
        return self
    
# ------------------------------------------------------------------------------------
    
    # Barcha numerical qiymatni MinMax orqali scaling qilish funksiyasi
    def scaling(self, target):
        
        try:
            num_column = self.df.select_dtypes(include=[np.number]).columns.tolist()
            
            if target in num_column:
                num_column.remove(target)
            
            if num_column:
                self.df[num_column] = self.minmax.fit_transform(self.df[num_column])
                loging.info("MinMax yordamida scaling qilindi")
                return self
        except Exception as e:
            loging.info(f"Scalin qilishda xatolik yuz berdi {e}")
    
# -------------------------------------------------------------------------------------
    
    # Preprocessed datani olish     
    def get_preprocessed_data(self):
        try:
            loging.info("Data preprocessing tugadi")
            return self.df
        except Exception as e:
            loging.info("Xatolik yuz berdi {e}")
        
# ---------------------------------------------------------------------     
            
    # preprocessed bolgan data ni saqlaydigan funksiya       
    def data_save(self):
        try:
            current_file = Path(__file__).resolve()
            project_folder = current_file.parent.parent

            data_path = project_folder/"data"/"preprocessed_data"
            data_path.mkdir(parents=True, exist_ok=True)
            full_data_path = data_path/"preprocessed_data.csv"
            self.df.to_csv(full_data_path, index = False)
            loging.info(f"Preprocessed data saqlandi {self.df.shape[0]} ta qator va {self.df.shape[1]} ta ustun")
    
        except Exception as e:
            loging.info("Datasetni saqlashda xatolik boldi")
# -----------------------------------------------------------------------