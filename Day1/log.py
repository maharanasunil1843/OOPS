import logging

logging.basicConfig(filename= "test.log", level = logging.INFO, format = "%(levelname)s %(name)s %(asctime)s %(message)s")
#Log levels: 1) Critical, 2) Error, 3) Warning, 4) INFO, 5) DEBUG
logging.info("This is my first code for logging")