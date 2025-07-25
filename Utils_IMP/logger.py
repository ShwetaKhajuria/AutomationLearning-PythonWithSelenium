import logging

logging.basicConfig(filename='C:/Users/khajuria_S/Desktop/PY/TestFiles/SeleniumLogs/test.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p'
                    )

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is info")

logger.warning("This is warning message")
logger.error("This is error")
logger.critical("This is critical message")