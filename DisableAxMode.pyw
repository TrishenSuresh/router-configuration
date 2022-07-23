import logging
from LoggerUtility import LoggerUtility
import WebDriverUtility
import RouterUtility

def disable_ax_mode():
    driver = WebDriverUtility.getHeadlessDriver()
    try:
        RouterUtility.disable_ax_mode(driver)
    except Exception as e:
        logger = LoggerUtility.init_logger()
        logger.error(e)
    finally:
        driver.close()

if __name__ == '__main__':
    disable_ax_mode()