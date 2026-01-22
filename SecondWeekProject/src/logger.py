import logging
import os
from pathlib import Path

def get_logger(log_file_name):
    # 1. logger.py faylining aniq manzilini topamiz
    # Bu kod qayerdan chaqirilishidan qat'i nazar, logger.py turgan joyni oladi
    current_file = Path(__file__).resolve()
    
    # 2. Loyiha asosiy papkasini (Root) topish
    # logger.py -> src papkasi -> Project papkasi (Root)
    # .parent (src) -> .parent (Project Root)
    project_root = current_file.parent.parent
    
    # 3. Logs papkasi manzilini yasash
    log_dir = project_root/"logs"

    # Papkani yaratish
    os.makedirs(log_dir, exist_ok=True)

    # Log fayl to'liq manzili
    log_path = log_dir / f"{log_file_name}.log"

    # Logger sozlamalari
    logger = logging.getLogger(log_file_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Path obyekti bo'lgani uchun stringga o'tkazamiz (str(log_path))
        file_handler = logging.FileHandler(str(log_path))
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)

    return logger

# Test qilib ko'rish uchun
if __name__ == "__main__":
    log = get_logger("test_run")
    log.info("Bu test log fayli.")









# import logging
# import os

# def get_logger(log_file_name):
#     # --- O'ZGARISH SHU YERDA ---
#     # 1. logger.py faylining o'zi turgan joyni aniqlaymiz
#     current_file_path = os.path.abspath(__file__) # .../Project/src/logger.py
    
#     # 2. Uning otasi (src) papkasini olamiz
#     src_dir = os.path.dirname(current_file_path) # .../Project/src
    
#     # 3. Uning ham otasi (Project) papkasini olamiz (Loyiha asosi)
#     project_root = os.path.dirname(src_dir)      # .../Project
    
#     # 4. Ana endi logs papkasini asosiy joyda yaratamiz
#     log_dir = os.path.join(project_root, "logs")
#     # ---------------------------
    
#     os.makedirs(log_dir, exist_ok=True)

#     log_path = os.path.join(log_dir, f"{log_file_name}.log")

#     logger = logging.getLogger(log_file_name)
#     logger.setLevel(logging.INFO)

#     if not logger.handlers:
#         file_handler = logging.FileHandler(log_path)
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)

#     return logger

# def get_logger(log_file_name):
#     """
#     Har bir chaqirilgan joy uchun alohida log fayli yaratib beruvchi funksiya.
    
#     Args:
#         log_file_name (str): Log faylining nomi (masalan, "data_cleaning").
#                              .log qo'shimchasi avtomatik qo'shiladi.
#     """
    
#     # 1. Loglar turadigan papkani aniqlash va yaratish
#     # Bu 'logs' papkasini loyiha asosiy papkasida ochadi
#     log_dir = os.path.join(os.getcwd(), "logs")
#     os.makedirs(log_dir, exist_ok=True)

#     # 2. To'liq fayl yo'lini yasash
#     log_path = os.path.join(log_dir, f"{log_file_name}.log")

#     # 3. Logger obyektini yaratish
#     # Har bir nom uchun alohida logger yaratiladi
#     logger = logging.getLogger(log_file_name)
#     logger.setLevel(logging.INFO)

#     # 4. Handler tekshiruvi (Dublikat yozuvlarni oldini olish uchun)
#     # Agar bu loggerda allaqachon handler bo'lsa, qayta qo'shmaymiz
#     if not logger.handlers:
#         # Faylga yozish uchun handler
#         file_handler = logging.FileHandler(log_path)
        
#         # Log formatini belgilash (Vaqt - Fayl nomi - Xabar turi - Xabar)
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_handler.setFormatter(formatter)
        
#         # Handlerni loggerga ulash
#         logger.addHandler(file_handler)

#     return logger