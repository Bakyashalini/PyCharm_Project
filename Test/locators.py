import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

#id

# txtusername = driver.find_element(By.ID, "email")
# txtusername.send_keys("shalini")
# txtpassword = driver.find_element(By.ID, "pass")
# txtpassword.send_keys("12435")
# btnlogin = driver.find_element(By.ID, "u_0_5_tf")
# btnlogin.click()
# time.sleep(4)

#name

txtusername = driver.find_element(By.NAME, "email")
txtusername.send_keys("shalini")
txtpassword = driver.find_element(By.NAME, "pass")
txtpassword.send_keys("12435")
btnlogin = driver.find_element(By.NAME, "login")
btnlogin.click()
time.sleep(4)

