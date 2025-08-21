import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

title = driver.title
print(title)

currurl = driver.current_url
print(currurl)

time.sleep(10)