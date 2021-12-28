from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver  = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.implicitly_wait(30)

coockie = driver.find_element_by_id('bigCookie')
coockie_counter = driver.find_element_by_id('cookies')
actions = ActionChains(driver)
items =  [driver.find_element_by_id('productPrice'+str(i)) for i in range(1,-1,-1)]
actions = ActionChains(driver)
actions.click(coockie)

for i in range (1000):
    actions.perform()
    count = int(coockie_counter.text.split(' ')[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrades_action =ActionChains(driver)
            upgrades_action.move_to_element(item)
            upgrades_action.click(item)
            upgrades_action.perform()    
