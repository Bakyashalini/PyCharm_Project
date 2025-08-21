import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

#  ClassName doesn't have space or underscore
# txtusername = driver.find_element(By.CLASS_NAME, "inputtext _55r1 _6luy")
# txtusername.send_keys("shalini")
# txtpassword = driver.find_element(By.CLASS_NAME, "inputtext _55r1 _6luy _9npi")
# txtpassword.send_keys("12435")
# btnlogin = driver.find_element(By.CLASS_NAME, "_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy")
# btnlogin.click()
# time.sleep(4)

# txtusername = driver.find_element(By.XPATH, "//input[@type='text']")
# txtusername.send_keys("shalini")
# txtpassword = driver.find_element(By.XPATH, "//input[@type='password']")
# txtpassword.send_keys("12435")
# btnlogin = driver.find_element(By.XPATH, "//button[@value='1']")
# btnlogin.click()
# time.sleep(4)

# btncreateacc = driver.find_element(By.XPATH, "(//a[@role='button'])[2]")
# btncreateacc.click()

btncreate = driver.find_elements(By.XPATH, "//a[@role='button']")
btncreateacc = btncreate[1]
btncreateacc.click()

