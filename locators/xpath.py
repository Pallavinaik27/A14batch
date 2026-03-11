'''Types of xpath
1)Absolute xpath
2)Relative xpath
'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

url1 = "https://testautomationpractice.blogspot.com/"
url2 = "https://demowebshop.tricentis.com/"

# driver.get(url2)
# driver.maximize_window()

# driver.find_element("xpath","//a[@class='ico-register']").click()
# sleep(3)
# driver.find_element("xpath","//input[@id='gender-female']").click()
# sleep(2)
# driver.find_element("xpath","//input[@name='FirstName' and @type='text']").send_keys("ABC")
# sleep(2)

#text()
# driver.find_element("xpath","//a[text()='Log in']").click()
# sleep(2)
# driver.find_element("xpath","//span[text()='Shopping cart']").click()
# sleep(2)
# shop = driver.find_element("xpath","//h1[text()='Shopping cart']")
# print(shop.text)
# driver.find_element("xpath","//a[text()='Register']").click()
# sleep(2)
# register = driver.find_element("xpath","//strong[text()='Your Personal Details']")
# print(register.text)


#contains
# driver.find_element("xpath","//a[contains(text(),'Computers')]").click()
# sleep(2)
# driver.find_element("xpath","//a[contains(text(),'Apparel')]").click()
# sleep(2)
# driver.find_element("xpath","//a[contains(@class,'register')]").click()
# sleep(2)
# driver.find_element("xpath","//input[contains(@id,'First')]").send_keys("ABCD")
# sleep(2)

#starts-with

# driver.find_element("xpath","//a[starts-with(@class,'ico-reg')]").click()
# sleep(2)
# driver.find_element("xpath","//input[starts-with(@name,'Last')]").send_keys("ABCD")
# sleep(2)

#indexing
driver.get(url1)
driver.maximize_window()

# driver.find_element("xpath","(//input[@class='form-control'])[2]").send_keys("abc@gmail.com")
# sleep(3)
# driver.find_element("xpath","(//button[@class='rectangular-button'])[3]").click()
# sleep(3)

#parent
# driver.find_element("xpath","//input[@id='name']/parent::div")
# driver.find_element("xpath","//th[text()='BookName']/parent::tr")
# driver.find_element("xpath","//textarea[@id='textarea']/parent::div")
# phone = driver.find_element("xpath","//div[@class='form-group'][1]/child::label[3]")
# print(phone.text)

#child
# driver.find_element("xpath","//div[@class='form-group'][2]/child::textarea").send_keys("This is python class")
# sleep(3)
# address = driver.find_element("xpath","//div[@class='form-group'][2]/child::label")
# print(address.text)
# h1 = driver.find_element("xpath","//div[@class='titlewrapper']/child::h1")
# print(h1.text)

#following-sibling
# value = driver.find_element("xpath","//td[text()='Amod']/following-sibling::td[1]")
# print(value.text)
# price = driver.find_element("xpath","//td[text()='Animesh']/following-sibling::td[2]")
# print(price.text)

#preceding-sibling
# bookname1 = driver.find_element("xpath","//td[text()='Animesh']/preceding-sibling::td")
# print(bookname1.text)
# bookname2 = driver.find_elements("xpath","//td[text()='Amit']/preceding-sibling::td")
# print(type(bookname2))
# print(bookname2)
#
# for book in bookname2:
#     print(book.text)

#ancestor
# table1 = driver.find_element("xpath","//th[text()='BookName']/ancestor::table")
# print(table1.get_attribute("name"))
# table2 = driver.find_element("xpath","//th[text()='Memory (MB)']/ancestor::table")
# print(table2.get_attribute("id"))

#descendant
tr1 = driver.find_elements("xpath","//table[@name='BookTable']/descendant::tr")
print(len(tr1))
tr2 = driver.find_elements("xpath","//table[@name='BookTable']/descendant::tr[2]/descendant::td")
for tr in tr2:
    print(tr.text)


driver.quit()