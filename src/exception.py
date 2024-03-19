import sys  #the sys module contains methods and variables for modifying many elements of the Python Runtime Environment
import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  #this exc_tb will store all the data that where the error actually is , it's line no.,file name
    file_name=exc_tb.tb_frame.f_code.co_filename   #this is the way to access the filename
    error_message="Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)   #super is used to give access to methods and properties of a parent or sibling class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
