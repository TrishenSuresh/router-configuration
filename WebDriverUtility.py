from selenium import webdriver
import pathlib

DRIVER_NAME = "chromedriver"

def getHeadlessDriver():
    path = pathlib.Path(__file__).parent.resolve().joinpath(DRIVER_NAME)
    options = webdriver.ChromeOptions()
    options.headless = True
    return webdriver.Chrome(path, options=options)