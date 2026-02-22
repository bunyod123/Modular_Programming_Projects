import logging
import os
from pathlib import Path

def get_logger(log_file_name):
    file_path = Path(__file__).resolve()
    project_file = file_path.parent.parent

    log_folder = project_file /"logs"
    os.makedirs(log_folder,exist_ok=True)

    log_file = log_folder/f"{log_file_name}.log"
    logger = logging.getLogger("log_file_name")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(str(log_file))
        formater = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        file_handler.setFormatter(formater)
        logger.addHandler(file_handler)
    return logger 
    

