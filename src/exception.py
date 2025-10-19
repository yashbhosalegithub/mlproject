import sys
import logging

def error_message_details(error, error_detail: sys):
    """Return a formatted error message with file name and line number."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    """Custom exception class for detailed error logging."""

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message


# Example usage:
try:
    a = 1 / 0
except Exception as e:
    raise CustomException(e, sys)
