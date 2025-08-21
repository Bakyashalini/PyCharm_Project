import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)

srch = driver.find_element(By.XPATH, "//input[@type='text']")
srch.send_keys("iphone", Keys.ENTER)
iphone = driver.find_element(By.XPATH, "//div[text()= 'Apple iphone16 (White, 128GB)']")
iphone.click()

#current window handle
parentId = driver.current_window_handle
print(parentId)

#windows handle
all_id = driver.windows_handle
print(all_id)

#switching into a window
driver.switch_to.window(all_id[1])
time.sleep(2)
cart = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
cart.click()

help = driver.find_element(By.XPATH, "//a[text()='Help Center']")
help.click()

parentId2 = driver.current_window_handle
print(parentId2)

all_id2 = driver.windows_handle
print(all_id2)

#switching into thr third window

driver.switch_to.window(all_id[2])
time.sleep(2)

