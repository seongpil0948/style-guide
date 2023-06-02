import logger
import sys

print(__name__)
log = logger.get_logger(__file__)
logger.setup_applevel_logger(file_name="gg.log")

def multiply(num1, num2): # just multiply two numbers
    log.debug("Executing multiply function.")
    return num1 * num2

multiply(1, 2)
