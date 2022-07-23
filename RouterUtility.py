from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import os

USER = os.getenv("ROUTER_USER")
PASSWORD = os.getenv("ROUTER_PASS")
URL = os.getenv("ROUTER_URL")

ADVANCED_WIRELESS_CONTENT_MENU = "#Advanced_Wireless_Content_menu .menu_Desc"
AX_MODE_SELECTOR = "wl_nmode_x"
LOGIN_USERNAME_FIELD = "login_username"
LOGIN_PASSWORD_FIELD = "login_passwd"

def login(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, LOGIN_USERNAME_FIELD)))
    driver.find_element(By.ID, LOGIN_USERNAME_FIELD).click()
    driver.find_element(By.ID, LOGIN_USERNAME_FIELD).send_keys(USER)
    driver.find_element(By.NAME, LOGIN_PASSWORD_FIELD).click()
    driver.find_element(By.NAME, LOGIN_PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, ".button").click()

def navigate_to_wireless_setting(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ADVANCED_WIRELESS_CONTENT_MENU)))
    driver.find_element(By.CSS_SELECTOR, ADVANCED_WIRELESS_CONTENT_MENU).click()

def select_ax_mode(driver, option):
    login(driver)
    navigate_to_wireless_setting(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, AX_MODE_SELECTOR)))
    driver.find_element(By.NAME, AX_MODE_SELECTOR).click()
    dropdown = driver.find_element(By.NAME, AX_MODE_SELECTOR)
    dropdown.find_element(By.XPATH, "//option[. = '{}']".format(option)).click()
    driver.find_element(By.ID, "applyButton").click()

def disable_ax_mode(driver):
    select_ax_mode(driver, "Auto")

def enable_ax_mode(driver):
    select_ax_mode(driver, "AX only")