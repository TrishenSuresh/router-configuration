from selenium.webdriver.common.by import By
import os

USER = os.getenv("ROUTER_USER")
PASSWORD = os.getenv("ROUTER_PASS")
URL = os.getenv("ROUTER_URL")

def login(driver):
    driver.get(URL)
    driver.find_element(By.ID, "login_username").click()
    driver.find_element(By.ID, "login_username").send_keys(USER)
    driver.find_element(By.NAME, "login_passwd").click()
    driver.find_element(By.NAME, "login_passwd").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, ".button").click()

def navigate_to_wireless_setting(driver):
    driver.find_element(By.CSS_SELECTOR, "#Advanced_Wireless_Content_menu .menu_Desc").click()

def select_ax_mode(driver, option):
    login(driver)
    navigate_to_wireless_setting(driver)
    driver.find_element(By.NAME, "wl_nmode_x").click()
    dropdown = driver.find_element(By.NAME, "wl_nmode_x")
    dropdown.find_element(By.XPATH, "//option[. = '{}']".format(option)).click()
    driver.find_element(By.ID, "applyButton").click()

def disable_ax_mode(driver):
    select_ax_mode(driver, "Auto")

def enable_ax_mode(driver):
    select_ax_mode(driver, "AX only")