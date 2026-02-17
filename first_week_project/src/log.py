from pathlib import Path
import os
import logging

def get_logger(log_file_name):
    
    current_file = Path(__file__).resolve()
    project_folder = current_file.parent.parent
    
    log_folder = project_folder/"logs"
    os.makedirs(log_folder, exist_ok = True)
    
    log_file = log_folder/f"{log_file_name}.log"
    
    logger = logging.getLogger(log_file_name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        file_handler = logging.FileHandler(str(log_file))
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
        