from selenium import webdriver
import time
# Instantiate chrome web driver
chrome_driver_path = "chromedriver/chromedriver.exe"
chrome_driver = webdriver.Chrome(chrome_driver_path)

chrome_driver.get("https://www.google.com")


search_bar = chrome_driver.find_element_by_id("lst-ib")
search_bar.send_keys("I want to learn web scraping")

search_bar.submit()
time.sleep(60)


chrome_driver.close()

