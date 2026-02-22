import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers = [
        logging.FileHandler('arithmeticOp.log')
    ]
)

logger = logging.getLogger('arithmeticOp') #This means creating a custom logger for each module or if the current module have any logger get that and logger hold that object 

def add(a,b) :
    result = a + b
    logger.debug(f"The addition of {a} + {b} = {result}")
    return result

def sub(a,b) :
    result = a - b
    logger.debug(f"The subtraction of {a} - {b} = {result}")
    return result

def mul(a,b) :
    result = a * b
    logger.debug(f"The multiplication of {a} * {b} = {result}")
    return result

def div(a,b) :
    try :
        result = a / b
        logger.debug(f"The division of {a} * {b} = {result}")
        return result
    except ZeroDivisionError :
        logger.error(f"The denominator is 0 cant divide {a} by {b}")


add(2,3)
sub(4,8)
mul(9,8)
div(2,0)