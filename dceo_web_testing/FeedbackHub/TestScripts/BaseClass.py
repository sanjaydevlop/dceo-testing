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
    def getLogger(self,ans):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)
        return logger
