import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers = [
        logging.FileHandler('arithmetic.log')
    ]
)

logger = logging.getLogger('arithmetic') #With this logger object we can create the logger message for custom module and for root logging message we can use logging.debug, etc

def add(a,b) :
    result = a + b
    logger.debug(f"The addition of {a} + {b} = {result}")
    return result

def sub(a,b) :
    result = a - b
    logger.debug(f"The subtraction of {a} - {b} = {result}")
    return result

add(2,3)
sub(5,6)