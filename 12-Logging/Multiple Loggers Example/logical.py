import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers = [
        logging.FileHandler('logical.log'),
        logging.StreamHandler() #whatever the log messages created stream at terminal too
    ]
)

logger = logging.getLogger('arithmetic')
# file_handler = logging.FileHandler('a.log')
# logger.addHandler(file_handler) #This basically tells the logger to where to send the log messages i.e inside the a.log file 

def andOperator(a,b) :
    result = a and b
    logger.debug(f"The logical and of {a} and {b} = {result}")
    return result

def orOperator(a,b) :
    result = a or b
    logger.debug(f"The logical or of {a} or {b} = {result}")
    return result

andOperator(1,0)
orOperator(1,0)