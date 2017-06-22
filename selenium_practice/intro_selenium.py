from selenium import webdriver
import time
# Instantiate chrome web driver
chrome_driver_path = "chromedriver/chromedriver.exe"
chrome_driver = webdriver.Chrome(chrome_driver_path)

chrome_driver.get("https://www.google.com")
time.sleep(5)

chrome_driver.close()
