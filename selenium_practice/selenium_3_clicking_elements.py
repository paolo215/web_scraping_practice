from selenium import webdriver
import time
# Instantiate chrome web driver
chrome_driver_path = "chromedriver/chromedriver.exe"
chrome_driver = webdriver.Chrome(chrome_driver_path)

chrome_driver.get("https://www.instagram.com")

login_button = chrome_driver.find_element_by_link_text("Log in")
login_button.click()


time.sleep(40)
chrome_driver.close()




