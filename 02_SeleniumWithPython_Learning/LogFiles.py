import logging

logging.basicConfig(filename='C:/Users/khajuria_S/Desktop/PY/TestFiles/SeleniumLogs/test.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p',
                    level=logging.DEBUG
                    )
# to print in format - time - which level and then Messgae - format='%(asctime)s: % (levelname)s:  %(message)s'

logging.debug("This is a debug message")
logging.info("This is info")

logging.warning("This is warning message")
logging.error("This is error")
logging.critical("This is critical message")