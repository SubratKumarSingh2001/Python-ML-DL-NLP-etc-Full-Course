import logging
import logging.config
from moduleA import moduleA_func
from moduleB import moduleB_func

def setup_config() :
    custom_config = {
        "version": 1,

        # ---------- FORMATTERS ----------
        "formatters": {
            'detailed' : {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                },
            'simple' : {
                'format': '%(asctime)s - %(levelname)s - %(message)s'
            }
        },

        # ---------- HANDLERS ----------
        "handlers": {
            #ROOT HANDLER
            "root_handlers" : {
                "class": "logging.FileHandler",
                "filename": "root.log",
                "formatter": "detailed",
                "level": "DEBUG"
            },

            # logger1 handler
            "moduleA_handler": {
               "class": "logging.FileHandler",
                "filename": "moduleA.log",
                "formatter": "detailed",
                "level": "DEBUG"
            },

            #logger2 handler
            "moduleB_handler": {
               "class": "logging.FileHandler",
                "filename": "moduleB.log",
                "formatter": "detailed",
                "level": "DEBUG"
            },

            #Common console handler for setup, logger1 and logger2
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "detailed",
                "level": "DEBUG"
            }
        },

        # ---------- ROOT LOGGER----------
        "root": {
            "handlers": ["root_handlers", "console"],
            "level": "DEBUG"
        },

        # ---------- CUSTOM LOGGERS WHICH ARE DEFINED INSIDE loggers, IF THERE IS NO CUSTOM LOGGER IT BY DEFAULT INHERITS THE ROOT LOGGER----------
        "loggers": {
            "moduleA": {
                "handlers": ["moduleA_handler"],
                "level": "DEBUG"
            },
            "moduleB":{
                "handlers": ["moduleB_handler"],
                "level": "DEBUG"
            }
        }
    }

    logging.config.dictConfig(custom_config)

if __name__ == '__main__' : #It is the starting point of the program when the program runs python setupConfig.py __name__ = __main__, and it checks the if statement satisfies then the entry point begin
    #calling the( setup_config() function for logging setup
    setup_config()

    #creating the setupConfig.py logger
    logger = logging.getLogger(__name__) #__name__ is the __main__ i.e __name__ = __main__ as we have executed the program __main__ logger is not present so it will inherit the root logger by default
    logger.info("setupConfig module started")

    moduleA_func()
    moduleB_func()

    logger.info("setupConfig module ended")