from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url1 = "https://practicetestautomation.com/practice-test-login/"
url2 = "https://demowebshop.tricentis.com/"
url3 = "https://testautomationpractice.blogspot.com/"
url4 = "https://www.amazon.in/"

#name
# driver.get(url1)
# driver.maximize_window()
#
# sleep(2)
#
# driver.find_element("name","username").send_keys("student")
# sleep(2)
# driver.find_element("name","password").send_keys("Password123")
# sleep(2)
# driver.find_element("id","submit").click()
# sleep(2)


#link_text
# driver.get(url2)
# driver.maximize_window()
#
# driver.find_element("link text","Register").click()
# sleep(3)
# driver.find_element("link text","Wishlist").click()
# sleep(2)
# driver.find_element("link text","Sitemap").click()
# sleep(2)
# driver.find_element("link text","Recently viewed products").click()
# sleep(3)


# driver.get(url3)
# driver.maximize_window()
#
# driver.find_element("link text","Udemy Courses").click()
# sleep(2)
# driver.back()
# sleep(2)
# driver.find_element("link text","Online Trainings").click()
# sleep(2)

# driver.get(url4)
# driver.maximize_window()
# sleep(5)
# driver.find_element("link text","Mobiles").click()


#partial_link_text
driver.get(url2)
driver.maximize_window()

driver.find_element("partial link text","Privacy").click()
sleep(3)
driver.find_element("partial link text","products").click()
sleep(3)
driver.find_element("partial link text","products list").click()
sleep(3)
driver.find_element("partial link text","ng & Ret").click()
sleep(3)
driver.find_element("partial link text","Books").click()
sleep(3)
driver.find_element("partial link text"," downloads").click()
sleep(3)

driver.quit()

