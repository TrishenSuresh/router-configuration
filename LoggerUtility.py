import pathlib
import logging

LOG_NAME = "selenium.log"
path = pathlib.Path(__file__).parent.resolve().joinpath(LOG_NAME)

class LoggerUtility:

    @staticmethod
    def init_logger():
        logging.basicConfig(filename=path, level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
        return logging