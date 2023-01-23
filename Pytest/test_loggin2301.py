import logging


def test_logsDemo():
    logger = logging.getLogger(__name__)  # __name__ catches test case name

    fileHandler = logging.FileHandler("logs.txt")  # describe file which is used for logs
    # format of logs
    format = logging.Formatter(
        "%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # example of tutor ;s is treating like a string

    fileHandler.setFormatter(format)  # adding format to file object
    logger.addHandler(fileHandler)  # to attach logs to file, requires usage of fileHandler object

    logger.setLevel(
        logging.INFO)  # define the level of logs needed (selected is used, and below it f.e. warning = warning,error,critical
    logger.debug("Debug log")
    logger.info("Info log")
    logger.warning("Warning log")
    logger.error("Error log")  # commonly used in failed assertions
    logger.critical("Critical log")