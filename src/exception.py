import sys 
import logging
"""  
sys module provides runtime environment variables and 
functions that interact directly with the Python interpreter. 
It allows you to control interpreter configurations, manage module paths, and capture command-line input. 
Unlike the os module (which interacts with the operating system), 
sys focuses strictly on the Python application environment itself.
"""

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in Python Script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    