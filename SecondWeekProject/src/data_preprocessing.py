import numpy as np
import pandas as pd
import os
import sys

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
minmax = MinMaxScaler()
labeller = LabelEncoder()

#--------------------------------------------------------------------------------------------------
# logger ni qoshamiz
sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\SecondWeekProject")
from src.logger import get_logger
logger = get_logger("data_preprocessing")

#--------------------------------------------------------------------------------------------------

class Preprocessing:
    def __init__(self,df):
         self.df = df.copy()
         self.encoder = LabelEncoder()
         self.scaler = MinMaxScaler()
         logger.info(f"Data Preprocessing boshlandi: {self.df.shape}")
        
  # -----------------------------------------------------------------------------------------
  
   # To'ldruvchi
    def fillingNan(self):
        try:
            num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            lab_cols = self.df.select_dtypes(exclude=[np.number]).columns.tolist()
            
            # Tekshirish: Agar ustunlar bo'lmasa xatolik bermasligi uchun
            if num_cols:
                num_imputer = SimpleImputer(strategy='mean')
                self.df[num_cols] = num_imputer.fit_transform(self.df[num_cols])
            
            if lab_cols:
                lab_imputer = SimpleImputer(strategy='most_frequent')
                self.df[lab_cols] = lab_imputer.fit_transform(self.df[lab_cols])
          
            logger.info("Nan qiymatlar toldirildi")
            return self  # <--- Muvaffaqiyatli bo'lsa qaytaradi
            
        except Exception as e:
            logger.error(f"Xatolik yuz berdi: {e}")
            raise e  # <--- MUHIM: Xatoni tashqariga chiqarish kerak!
 
 # -----------------------------------------------------------------------------------------------   
        
# Encoding qiluvchi
    def encoding_qilish(self):
        try:
            for col in self.df.columns:
                if self.df[col].dtype == 'object':
                    if self.df[col].nunique() <= 5:
                        dummies = pd.get_dummies(self.df[col], prefix=col, dtype=int)
                        self.df = pd.concat([self.df.drop(columns=[col]), dummies], axis=1)
                    else:
                        self.df[col] = self.encoder.fit_transform(self.df[col])
            logger.info("Encoding qilindi")
            return self
        except Exception as e:
            logger.error(f"Xatolikbor encoding qilishda {e}")
            raise e
     
 # -----------------------------------------------------------------------------------------------   
 
      # Log transforming
    def logTransformation(self):
        try:
            skewness = self.df.skew()
            features_log = skewness[skewness >= 0.5].index.tolist()
            for col in features_log:
                if (self.df[col] > 0).all():
                    self.df[col] = np.log1p(self.df[col])
            logger.info("Log transforming qilindi")
            return self
        except Exception as e:
            logger.error("Log tranform qilish da xatolik boldi")
            raise e
    
    # ---------------------------------------------------------------------------------------
    
# Scale qiluvchi
    def scaling(self):
        try:

            num_cols = self.df.select_dtypes(include=[np.number]).columns.drop('price_range').tolist()
            self.df[num_cols] = self.scaler.fit_transform(self.df[num_cols])

            logger.info("Scaling qilindi")
            return self
        
        except Exception as e:
            logger.error("Scaling qilishda muammo boldi")
            raise e
    
    # ---------------------------------------------------------------------------------------------
        
    # Final data ni olish
    def getDataset(self):
        return self.df
    
# Datani saqlash
    # def saqlash(self):
    #     folder = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\SecondWeekProject\data\preprocessed_data"    
    #     path = os.path.join(folder, "preprocessed_data.csv")
    #     df.to_csv(path, index = False)
  