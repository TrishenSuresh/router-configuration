import WebDriverUtility
import RouterUtility

def enable_ax_mode():
    driver = WebDriverUtility.getHeadlessDriver()
    try:
        RouterUtility.enable_ax_mode(driver)
    finally:
        driver.close()

if __name__ == '__main__':
    enable_ax_mode()