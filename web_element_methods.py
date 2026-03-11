from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

url1 = "https://testautomationpractice.blogspot.com/"
url2 = "https://the-internet.herokuapp.com/dynamic_controls"

# driver.get(url1)
# driver.maximize_window()

#Action methods
#send_keys(), click(), clear()
# name = driver.find_element("id","name")
# name.send_keys("ABC")
# sleep(3)
# name.clear()
# sleep(3)
# name.send_keys("XYZ")
# sleep(3)
#
# textarea = driver.find_element("id","textarea")
# textarea.send_keys("This is manual testing class")
# sleep(2)
# textarea.clear()
# sleep(2)
# textarea.send_keys("This is Automation Testing class")
# sleep(3)

#------------------------------------------------------------------------
#Validation methods

#is_displayed

# text_ = driver.find_element("xpath","//span[text()='For Selenium, Cypress & Playwright']")
# print(text_.is_displayed())

# h2 = driver.find_element("xpath","//h2[text()='Pages']")
# print(h2.is_displayed())

#is_enabled()
# driver.get(url1)
# driver.maximize_window()

# name = driver.find_element("id","name")
# print(name.is_enabled())

# checkbox = driver.find_element("id","sunday")
# print(checkbox.is_enabled())

# driver.get(url2)
# driver.maximize_window()
#
# textbox = driver.find_element("xpath","//form[@id='input-example']/input")
# print(textbox.is_enabled())


#is_selected
# driver.get(url1)
# driver.maximize_window()


# male = driver.find_element("id","male")
# print(male.is_selected())
#
# female = driver.find_element("id","female")
# female.click()
# sleep(2)
# print(female.is_selected())

# sunday = driver.find_element("id","sunday")
# sunday.click()
# sleep(2)
# print(sunday.is_selected())
#
# monday = driver.find_element("id","monday")
# print(monday.is_selected())


#-------------------------------------------------------------------------------------------
#Location and size methods

driver.get(url1)
driver.maximize_window()

#location
start = driver.find_element("css selector",".start")
print(f"location of start button : {start.location}")

text1 = driver.find_element("xpath","//h2[text()='Mouse Hover']")
print(f"location of text1 : {text1.location}")

link = driver.find_element("link text","Udemy Courses")
print(f"location of link : {link.location}")

#size
print(f"size of start button : {start.size}")
print(f"size of text1 : {text1.size}")
print(f"size of link : {link.size}")

#rect
print(f"rect of start button : {start.rect}")
print(f"rect of text1 : {text1.rect}")
print(f"rect of link : {link.rect}")


driver.quit()