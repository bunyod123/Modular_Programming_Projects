import logging
import os
from pathlib import Path

def get_logger(log_file_name):
    # 1. logger.py faylining aniq manzili
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent
    
    # 3. Logs papkasi manzilini yasash
    log_dir = project_root/"logs"
    os.makedirs(log_dir, exist_ok=True)

    # Log fayl to'liq manzili
    log_path = log_dir / f"{log_file_name}.log"
    
    logger = logging.getLogger(log_file_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        
        file_handler = logging.FileHandler(str(log_path))
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)

    return logger