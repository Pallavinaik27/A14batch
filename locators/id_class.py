from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

url1 = "https://testautomationpractice.blogspot.com/"
url2 = "https://demowebshop.tricentis.com/"

# driver.get(url1)
# driver.maximize_window()

#id
# name = driver.find_element("id","name")
# name.send_keys("Prajatka")
# sleep(2)
#
# driver.find_element("id","email").send_keys("sharvani@gmail.com")
# sleep(2)
#
# driver.find_element("id","phone").send_keys("9876543210")
# sleep(2)
#
# driver.find_element("id","textarea").send_keys("This is Python selenium class")
# sleep(2)


#class name
# driver.find_element("class name","form-control").send_keys("Anjana")
# sleep(2)
#
# driver.find_element("class name","wikipedia-search-input").send_keys("Automation")
# sleep(3)
#
# driver.find_element("class name","start").click()
# sleep(3)
#
# title = driver.find_element("class name","title")
# print(title.text)
#
# driver.find_element("class name","Header")



driver.get(url2)
driver.maximize_window()

driver.find_element("class name","ico-register").click()
sleep(2)
driver.find_element("id","gender-female").click()
sleep(2)
driver.find_element("class name","single-line").send_keys("Manova")
sleep(2)
driver.find_element("id","LastName").send_keys("Steev")
sleep(2)
driver.find_element("id","Email").send_keys("manova@gmail.com")
sleep(2)
driver.find_element("class name","password").send_keys("12345678")
sleep(2)
driver.find_element("id","ConfirmPassword").send_keys("12345678")
sleep(2)
driver.find_element("class name","register-next-step-button").click()
sleep(2)


driver.quit()
