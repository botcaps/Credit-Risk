import logging
import os
from datetime import datetime

# Generate a unique log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%M_%d_%Y_%H_%M_%S')}.log"  # Use '%d' instead of '%D' to avoid slashes

# Define the path for the log file directory
log_path = os.path.join(os.getcwd(), "log")  # Separate directory and file name

# Create the directory for log files if it doesn't already exist
os.makedirs(log_path, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Basic logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file path
    level=logging.INFO,      # Set the logging level to INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define log message format
)

# Example log usage to verify logging setup
logging.info("Logging has been set up successfully.")
