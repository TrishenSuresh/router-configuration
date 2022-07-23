from LoggerUtility import LoggerUtility
import WebDriverUtility
import RouterUtility

def enable_ax_mode():
    driver = WebDriverUtility.getHeadlessDriver()
    try:
        RouterUtility.enable_ax_mode(driver)
    except Exception as e:
        logger = LoggerUtility.init_logger()
        logger.error(e)
    finally:
        driver.close()

if __name__ == '__main__':
    enable_ax_mode()