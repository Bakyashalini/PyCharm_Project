import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://greenstech.in/selenium-course-content.html")
# driver.maximize_window()
# a = ActionChains(driver)
#
# txtcourses = driver.find_element(By.XPATH, "//div[@title='Courses']")
# a.move_to_element(txtcourses).perform()
#
# txtswtesting = driver.find_element(By.XPATH, "//span[text()='Software Testing (12)']")
# a.move_to_element(txtswtesting).perform()
#
# btnselenium = driver.find_element(By.XPATH, "//span[text()='Selenium Certification Training']")
# a.click(btnselenium).perform()
#
# time.sleep(4)

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()
a = ActionChains(driver)

src = driver.find_element(By.XPATH, "//a[text()=' 5000']")
des = driver.find_element(By.ID, "amt8")

a.drag_and_drop(src, des).perform()
a.click_and_hold(src).release(des).perform()
a.click_and_hold(src).move_to_element(des).release().perform()
time.sleep(3)
