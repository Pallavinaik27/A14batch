from selenium import webdriver


driver = webdriver.Chrome()

url1 = "https://testautomationpractice.blogspot.com/"
url2 = "https://artoftesting.com/samplesiteforselenium?utm_source=chatgpt.com"

#css selector
# name = driver.find_element("css selector","#name")
# name.send_keys("ABC")
# sleep(2)
# name.clear()
#
# driver.find_element("css selector",".form-control").send_keys("XYZ")
# sleep(2)

# input_tags = driver.find_elements("css selector","input")
# print(len(input_tags))

# driver.get(url2)
# driver.maximize_window()
#
# h1 = driver.find_element("css selector",".gb-headline.gb-headline-a55ce89a.gb-headline-text")
# print(h1.text)
# sleep(2)
#
# submit = driver.find_element("css selector","button[title='Hovering over me!!']")
# submit.click()
# sleep(3)
#
# checkbox = driver.find_element("css selector","input[type='checkbox'][value='Automation']")
# checkbox.click()
# sleep(3)

#-------------------------------------------------------------------------------------------------

# driver.get(url1)
# driver.maximize_window()

# driver.find_element("css selector","input[class='form-check-input']").click()
# sleep(3)

# all_checkboxes = driver.find_elements("css selector","input[type='checkbox']")
# for checkbox in all_checkboxes:
#     checkbox.click()
#     sleep(2)
#
# days_checkboxes = driver.find_elements("css selector","input[class='form-check-input'][type='checkbox']")
# for checkbox in days_checkboxes:
#     checkbox.click()
#     sleep(2)

#-------------------------------------------------------------------------------------------------
# driver.get(url2)
# driver.maximize_window()

# driver.find_element("css selector","button[id^='idOf']").click()
# sleep(3)
# driver.find_element("css selector","input[id^='fem']").click()
# sleep(3)
#
# driver.find_element("css selector","input[class$='mation']").click()
# sleep(3)
# driver.find_element("css selector","input[class$='mance']").click()
# sleep(3)

# h1 = driver.find_element("css selector","h1[class*='gb-headline-a55c']")
# print(h1.text)
# name = driver.find_element("css selector","input[name*='stNa']")
# name.send_keys("ABCD")
# sleep(3)

# text1 = driver.find_element("css selector",".entry-content p")
# print(text1.text)

# text2 = driver.find_element("css selector",".entry-content div p")
# print(text2.text)

#direct child
# text3 = driver.find_element("css selector",".entry-content > div")
# print(text3.text)
# text4 = driver.find_element("css selector","#commonWebElements > p")
# print(text4.text)
# text5 = driver.find_element("css selector","#commonWebElements > form")
# print(text5.text)
# text6 = driver.find_element("css selector","#AlertBox > p")
# print(text6.text)

#adjacent sibling
# text7 = driver.find_element("css selector",".entry-content > p + p")
# print(text7.text)
# text8 = driver.find_element("css selector","#idOfDiv + p")
# print(text8.text)

#general sibling
# text9 = driver.find_element("css selector","#idOfDiv ~ form")
# print(text9.text)
#
# text10 = driver.find_elements("css selector","#idOfDiv ~ form")
# for text_ in text10:
#     print(text_.text)
#
# text11 = driver.find_elements("css selector","#idOfDiv ~ p")
# for text_ in text11:
#     print(text_.text)


#first child
# text12 = driver.find_element("css selector",".entry-content p:first-child")
# print(text12.text)

# text13 = driver.find_element("css selector",".entry-content div:last-child")
# print(text13.text)

# text14 = driver.find_element("css selector","#commonWebElements p:nth-child(2)")
# print(text14.text)


driver.get(url1)
driver.maximize_window()

# text15 = driver.find_element("css selector","table[name='BookTable'] th:first-child")
# print(text15.text)
#
# text16 = driver.find_element("css selector","table[name='BookTable'] th:last-child")
# print(text16.text)
#
# text17 = driver.find_element("css selector","table[name='BookTable'] th:nth-child(3)")
# print(text17.text)

text18 = driver.find_element("css selector","table[name='BookTable'] tr:nth-child(2) td:nth-child(4)")
print(text18.text)


driver.quit()

