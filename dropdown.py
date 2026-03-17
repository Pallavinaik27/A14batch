from time import  sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url1 = "https://testautomationpractice.blogspot.com/"
url2 = "https://semantic-ui.com/modules/dropdown.html"
url3 = "https://www.flipkart.com/"


#single select

# driver.get(url1)
# driver.maximize_window()

# country = driver.find_element("id","country")
# sleep(2)

# option = Select(country)
# option.select_by_index(9)
# sleep(3)
# option.select_by_visible_text("Canada")
# sleep(3)
# option.select_by_value("germany")
# sleep(3)

#---------------------------------------------------------------------------------------------
#multiselect
# colors = driver.find_element("id","colors")
#
# option = Select(colors)
# option.select_by_index(1)
# sleep(2)
# option.select_by_value("green")
# sleep(2)
# option.select_by_visible_text("White")
# sleep(2)
#
# selected_options = option.all_selected_options
# print(len(selected_options))
# print([select.text for select in selected_options])
#
# option.deselect_by_value("blue")
# sleep(2)
# option.deselect_all()
# sleep(3)

# print(option.is_multiple)

#--------------------------------------------------------------------------------
#Without select tag

# driver.get(url2)
# driver.maximize_window()
#
# dropdown = driver.find_element("css selector",".ui.selection.dropdown")
# dropdown.click()
# sleep(3)
#
# driver.find_element("xpath","//div[text()='Female']").click()
# sleep(3)


#--------------------------------------------------------------------------------
#Auto select dropdown

driver.get(url3)
driver.maximize_window()
sleep(4)

search = driver.find_element("xpath","//input[@title='Search for Products, Brands and More']")
search.send_keys("iphone")
sleep(4)

options = driver.find_elements("xpath","//div[@class='VDtK0l _1psv1ze2u _1psv1ze53 _1psv1ze9x _1psv1ze7o']")
for option in options:
    if "iphone 13" in option.text:
        option.click()
        sleep(4)
        break



driver.quit()

