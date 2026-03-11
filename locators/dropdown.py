from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

driver.maximize_window()
sleep(3)

search = driver.find_element("xpath","//input[@title='Search for Products, Brands and More']")
search.send_keys("iphone")
sleep(5)

items = driver.find_elements("xpath","//form[contains(@class,'header-form-search')]//a")
print(len(items))
for item in items:
    if 'iphone 16' in item.text:
        item.click()
        sleep(4)
        break