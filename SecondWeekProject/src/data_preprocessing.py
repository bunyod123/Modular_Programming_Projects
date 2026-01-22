import numpy as np
import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

minmax = MinMaxScaler()
labeller = LabelEncoder()






class Preprocessing:
    def __init__(self,df):
        self.df = df
        
# Encoding qiluvchi
    def encoding_qilish(self):
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                if self.df[col].nunique() <= 3:
                    new_df = pd.get_dummies(self.df[col], prefix='New', dtype=int)
                    self.df.drop(columns=[col],inplace=True)
                    self.df = pd.concat([self.df,new_df],axis=1)
                else:
                    self.df[col] = labeller.fit_transform(self.df[col])
        return self
    

# To'ldruvchi
    def fillingNan(self):
        for cols in self.df.columns:
            if self.df[cols].isnull().any():
                if self.df[cols].dtype == 'object':
                    self.df[cols].fillna(self.df[cols].mode()[0], inplace=True)
                else:
                    self.df[cols].fillna(self.df[cols].mean(),inplace=True)
        return self
    
    
# Scale qiluvchi
    def scaling_qilish(self): 
        for cols in self.df.columns: 
            if self.df[cols].dtype != 'object' and self.df[cols].name != 'WIND': 
                self.df[cols] = minmax.fit_transform(self.df[[cols]]) 
        return self.df
    
    
# Datani saqlash
    def saqlash(self):
        folder = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\SecondWeekProject\data\preprocessed_data"    
        path = os.path.join(folder, "preprocessed_data.csv")
        df.to_csv(path, index = False)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    folder = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\FirstWeekProject\data\preprocessed_data"
path = os.path.join(folder,'preprocessed_data.csv')
df1.to_csv(path, index=False)