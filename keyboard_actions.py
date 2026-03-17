from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

actions = ActionChains(driver)

name = driver.find_element("id","name")
email = driver.find_element("id","email")
address = driver.find_element("id","textarea")
dropdown = driver.find_element("id","country")

# name.send_keys("ABCD")
# sleep(3)
#
# name.send_keys(Keys.CONTROL + 'a')
# sleep(4)
# name.send_keys(Keys.CONTROL + 'c')
#
# email.send_keys(Keys.CONTROL + 'v')
# sleep(4)
# email.send_keys(Keys.CONTROL + 'a')
# sleep(3)
# email.send_keys(Keys.CONTROL + 'x')
# sleep(3)
#
# address.send_keys(Keys.CONTROL + 'v')
# sleep(3)
# address.send_keys(Keys.BACKSPACE)
# sleep(3)
# address.send_keys(Keys.CONTROL + 'a')
# address.send_keys(Keys.DELETE)
# sleep(3)

# name.send_keys(Keys.PAGE_DOWN)
# sleep(3)
# name.send_keys(Keys.PAGE_DOWN)
# sleep(4)
# dropdown.send_keys(Keys.PAGE_UP)
# sleep(3)

actions.click(name)
actions.pause(3)
actions.key_down(Keys.SHIFT)
actions.send_keys("XYZ")
sleep(3)


driver.quit()
