import logging

def moduleB_func() :
    logger2 = logging.getLogger(__name__) #__name__ = moduleB
    logger2.debug("This is Debug message")
    logger2.info("This is info message")
    logger2.warning("This is warning messages")
    logger2.error("This is error message")
    logger2.critical("This is critical message")   