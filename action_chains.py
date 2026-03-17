from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(3)

actions = ActionChains(driver)

#mouse hover
# start = driver.find_element("xpath","//button[text()='START']")
# actions.move_to_element(start).perform()
# sleep(3)
# actions.click(start).perform()

# sleep(4)
#
# mouse_hover = driver.find_element("xpath","//button[text()='Point Me']")
# actions.move_to_element(mouse_hover).perform()
# sleep(4)

#-----------------------------------------------------
#right click

# home = driver.find_element("link text","Home")
# actions.context_click(home).perform()
# sleep(4)
#
# files = driver.find_element("link text","Download Files")
# actions.context_click(files).perform()
# sleep(4)

#---------------------------------------------------------
#double click
#
# copy_text = driver.find_element("xpath","//button[text()='Copy Text']")
# actions.double_click(copy_text).perform()
# sleep(4)

#---------------------------------------------------------
#drag and drop

# draggable = driver.find_element("id","draggable")
# droppable = driver.find_element("id","droppable")
# actions.drag_and_drop(draggable,droppable).perform()
# sleep(4)

#--------------------------------------------------------------------------------------
#drag and drop by offset

slider1 = driver.find_element("xpath","//div[@id='slider-range']/child::span[1]")
slider2 = driver.find_element("xpath","//div[@id='slider-range']/child::span[2]")
# actions.drag_and_drop_by_offset(slider1,50,0).perform()
# sleep(3)
# actions.drag_and_drop_by_offset(slider2,30,0).perform()
# sleep(4)

# actions.drag_and_drop_by_offset(slider1,-20,0).perform()
# sleep(3)
# actions.drag_and_drop_by_offset(slider2,-50,0).perform()
# sleep(3)

# actions.drag_and_drop_by_offset(slider1,120,0).perform()
# sleep(3)
# actions.drag_and_drop_by_offset(slider2,-120,0).perform()
# sleep(3)

actions.drag_and_drop_by_offset(slider2,120,0).perform()
sleep(3)
actions.drag_and_drop_by_offset(slider1,-50,0).perform()
actions.drag_and_drop_by_offset(slider1,290,0).perform()
sleep(3)

driver.quit()


