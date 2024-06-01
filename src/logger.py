# src/logger.py
import logging
import os

def setup_logging():
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'app.log')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=log_path,
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
