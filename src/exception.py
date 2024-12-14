import sys

# Function to generate detailed error messages
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback information
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the error occurred
    error_message = (
        f"Error occurred in Python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    )
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the base class constructor
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
