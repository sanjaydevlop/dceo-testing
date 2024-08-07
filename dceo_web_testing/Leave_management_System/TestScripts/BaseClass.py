import pytest
import inspect
import logging
import os,sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
print(parent_dir)

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self,test_file_name):
        loggerName = inspect.stack()[1][3]
        # log_file_name = f"{test_file_name}_logfile.log"
        # log_file_path = os.path.join(parent_dir, "reports", log_file_name)
        logger = logging.getLogger(loggerName)
        # fileHandler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # fileHandler.setFormatter(formatter)
        # logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
