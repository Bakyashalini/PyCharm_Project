import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

# txt = driver.find_element(By.XPATH, "//a[text()='Create a Page']")
# txt1 = txt.text
# print(txt1)
# txt.click()

txt2 = driver.find_element(By.XPATH, "//div[text()=' for a celebrity, brand or business.']")
txt2 = txt2.text
print(txt2)

txt3 = driver.find_element(By.XPATH, "//h2[contains(text(), 'Facebook')]")
txt4 = txt3.text
print(txt4)
time.sleep(3)

