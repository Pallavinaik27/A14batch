from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

url1 = "https://demoqa.com/frames"
url2 = "https://demo.automationtesting.in/Frames.html"


# driver.get(url1)
# driver.maximize_window()
#
#
# driver.switch_to.frame("frame1")
# h1 = driver.find_element("xpath","//h1[text()='This is a sample page']")
# print(h1.text)


#----------------------------------------------------
driver.get(url2)
driver.maximize_window()

#single iframe
# driver.switch_to.frame("SingleFrame")
# driver.find_element("xpath","//input[@type='text']").send_keys("ABCD")
# sleep(3)

#------------------------------------------------------------
#Nested iframe

driver.find_element("xpath","//a[@href='#Multiple']").click()
sleep(2)

outer_iframe = driver.find_element("xpath","//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_iframe)
h5 = driver.find_element("xpath","//h5[text()='Nested iFrames']")
print(h5.text)


inner_iframe = driver.find_element("xpath","//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_iframe)
text_ = driver.find_element("xpath","//h5[text()='iFrame Demo']")
print(text_.text)
driver.find_element("xpath","//input[@type='text']").send_keys("ABCD")
sleep(3)


#---------------------------------------------------------------------------
# driver.switch_to.parent_frame()
# print(h5.text)


#-------------------------------------------------------------------------
driver.switch_to.default_content()
driver.find_element("xpath","//a[@href='#Single']").click()
sleep(4)

driver.quit()