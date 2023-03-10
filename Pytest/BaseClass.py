import inspect
import logging

class BaseClass:
    def getLogger(self):

        loggerName = inspect.stack()[1][3]#improvement to properly display test_ methods in logs when using this method as inherited.
        logger = logging.getLogger(loggerName)  # __name__ catches test case name

        fileHandler = logging.FileHandler("logs.txt")  # describe file which is used for logs
        # format of logs
        format = logging.Formatter(
            "%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # example of tutor ;s is treating like a string

        fileHandler.setFormatter(format)  # adding format to file object
        logger.addHandler(fileHandler)  # to attach logs to file, requires usage of fileHandler object

        logger.setLevel(
            logging.INFO)  # define the level of logs needed (selected is used, and below it f.e. warning = warning,error,critical
        return logger #method will return logger (logging object)