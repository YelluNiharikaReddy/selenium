import logging

logging.basicConfig(filename= "C://Users/Dell/Desktop/New folder/demo.log",
                    format="%(asctime)s :%(levelname)s :%(message)s",
                    datefmt="%m/%d/%y %I:%M:%S %p",level=logging.DEBUG)

logger =logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("this is debug msg")
logger.warning("this is waring msg")
logger.critical("this is critical msg")
logger.info("this is info msg")
logger.error("this is error msg")
