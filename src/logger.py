# src/logger.py
import logging
import os


def setup_logging():
    # Calculate the absolute path to the logs directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_directory = os.path.join(base_dir, 'logs')

    # Create the logs directory if it doesn't exist
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    # Define the full path to the log file
    log_path = os.path.join(logs_directory, 'app.log')

    # Print the log path to verify it (you can remove this after confirming the path)
    print("Logging to:", log_path)

    # Set up logging configuration
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=log_path,
                        filemode='a')

    # Set up console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
