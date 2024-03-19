import logging
#This module defines functions and classes which implement a flexible event logging system for applications and libraries.
#The key benefit of having the logging API provided by a standard library module is that all Python modules can participate 
#in logging, so your application log can include your own messages integrated with messages from third-party modules
import os #os module with methods for interacting with the operating system, like creating files and directories, management of files and directories

from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Name of the log file with its specified format
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #directory of th elog file
os.makedirs(logs_path,exist_ok=True) #to avoid raising any exception or issue if the log file exits before

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #Final path former by merging the logs path and logs file.

logging.basicConfig( #contetnts of the log file
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  #only add the data if they are upto the security level of INFO


)

if __name__ == "__main__":
    logging.info("Logging has started")