from selenium import webdriver
import time
# Instantiate chrome web driver
chrome_driver_path = "webdriver/chromedriver"
chrome_driver = webdriver.Chrome(chrome_driver_path)
print("before sleep")
time.sleep(5)
print("after sleep")

driver.close()
