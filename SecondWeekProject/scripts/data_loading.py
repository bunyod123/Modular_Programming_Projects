import os, sys

path = sys.path.append(r"C:\Users\bunyo\oneDrive\desktop\AI_Course\ModularProgramProjects\SecondWeekProject")

from src.data_loading import DataLoad

data_link = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\SecondWeekProject\data\raw_data\train.csv"

loading = DataLoad(data_link)

df = loading.data_loader()

print(df.head())









import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

class DataPreprocessor:
    """
    Ma'lumotlarni yuklash, tozalash va model uchun tayyorlash 
    vazifasini bajaruvchi class.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        """Ma'lumotlarni CSV fayldan o'qiydi."""
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"✅ Ma'lumot yuklandi. Hajmi: {self.df.shape}")
            return self.df
        except Exception as e:
            print(f"❌ Xatolik yuz berdi: {e}")
            return None

    def handle_missing_values(self, strategy='mean'):
        """
        Yetishmayotgan (NaN) qiymatlarni to'ldiradi.
        strategy: 'mean' (o'rtacha), 'median', yoki 'most_frequent' (eng ko'p uchraydigan).
        """
        if self.df is not None:
            # Faqat raqamli ustunlarni ajratib olamiz
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            
            imputer = SimpleImputer(strategy=strategy)
            self.df[numeric_cols] = imputer.fit_transform(self.df[numeric_cols])
            
            print(f"🛠 Yetishmayotgan qiymatlar '{strategy}' usuli bilan to'ldirildi.")
        return self.df

    def encode_categorical_data(self, target_column):
        """
        Matnli (kategorik) ustunlarni raqamga o'giradi.
        Target ustun uchun LabelEncoding, qolganlari uchun OneHotEncoding (yoki oddiyroq usul) ishlatilishi mumkin.
        Bu misolda soddalik uchun LabelEncoder ishlatamiz.
        """
        if self.df is not None:
            le = LabelEncoder()
            # Barcha object turidagi ustunlarni aylanib chiqamiz
            for col in self.df.select_dtypes(include=['object']).columns:
                self.df[col] = le.fit_transform(self.df[col])
            
            print("🔢 Kategorik ma'lumotlar raqamlashtirildi.")
        return self.df

    def split_data(self, target_column, test_size=0.2, random_state=42):
        """
        Ma'lumotni Train va Test qismlarga ajratadi.
        """
        if self.df is not None:
            X = self.df.drop(columns=[target_column])
            y = self.df[target_column]

            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            print(f"✂️ Ma'lumot ajratildi: Train ({self.X_train.shape}), Test ({self.X_test.shape})")
            return self.X_train, self.X_test, self.y_train, self.y_test

    def scale_features(self):
        """
        Xususiyatlarni (features) standartlashtirish (Scaling).
        Bu modelning aniqligini oshirish uchun muhim.
        """
        if self.X_train is not None:
            scaler = StandardScaler()
            self.X_train = scaler.fit_transform(self.X_train)
            self.X_test = scaler.transform(self.X_test)
            print("⚖️ Ma'lumotlar shkalalandi (StandardScaler).")
            return self.X_train, self.X_test

# --- TEST QILISH UCHUN (Faqat shu fayl ishga tushganda ishlaydi) ---
if __name__ == "__main__":
    # Namuna uchun:
    # Fayl yo'lini to'g'irlang (masalan: 'data/housing.csv')
    processor = DataPreprocessor('data.csv') 
    
    # 1. Yuklash
    df = processor.load_data()
    
    if df is not None:
        # 2. Tozalash
        processor.handle_missing_values()
        
        # 3. Raqamlashtirish (Target ustun nomini o'zingizga moslang, masalan 'price' yoki 'class')
        processor.encode_categorical_data(target_column='target')
        
        # 4. Ajratish
        processor.split_data(target_column='target')
        
        # 5. Shkalalash
        processor.scale_features()
        
        print("\n✅ Preprocessing yakunlandi!")