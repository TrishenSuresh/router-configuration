import WebDriverUtility
import RouterUtility

def disable_ax_mode():
    driver = WebDriverUtility.getHeadlessDriver()
    try:
        RouterUtility.disable_ax_mode(driver)
    finally:
        driver.close()

if __name__ == '__main__':
    disable_ax_mode()