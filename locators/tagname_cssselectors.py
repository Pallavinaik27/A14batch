from selenium import webdriver

driver = webdriver.Chrome()

url1 = "https://testautomationpractice.blogspot.com/"
url2 = "https://artoftesting.com/samplesiteforselenium?utm_source=chatgpt.com"

# driver.get(url1)
# driver.maximize_window()

#tag name

# h1 = driver.find_element("tag name","h1")
# print(h1.text)
#
# button = driver.find_element("tag name","button")
# button.click()

# buttons = driver.find_elements("tag name","button")
# print(len(buttons))
#
# for button in buttons:
#     button.click()
#     sleep(2)

# p = driver.find_elements("tag name","p")
# print(len(p))
# for p_text in p:
#     print(p_text.text)






driver.quit()