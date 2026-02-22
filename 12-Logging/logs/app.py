import logging
#We can directly import the .py modules which lies within the same directory, if logger.py would have been in another directory, then we would be needed to make that folder package first then import
import logger #This ensure that the basic configuration of logging is set up

def add(a,b) :
    logging.debug("The addition operation is taking place")

logging.debug("The addition function is being called")
add(3,4)