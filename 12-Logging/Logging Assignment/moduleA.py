import logging

def moduleA_func() :
    logger1 = logging.getLogger(__name__) #__name__ = moduleA
    logger1.debug("This is Debug message")
    logger1.info("This is info message")
    logger1.warning("This is warning messages")
    logger1.error("This is error message")
    logger1.critical("This is critical message")   