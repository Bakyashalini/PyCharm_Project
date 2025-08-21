import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

# driver = webdriver.Firefox()
# driver.get("https://www.facebook.com/")

# driver = webdriver.Edge()
# driver.get("https://www.facebook.com/")

driver.quit()

