from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

#-----------------DEFAULT CONFIG

options = Options()
options.headless = True
PATH = '/Users/adammcmurchie/2021/selenium/chromedriver'
driver = webdriver.Chrome(PATH,options=options)

#-----------------SET WEBSITE
driver.get('https://techwithtim.net')


#-----------------SET ELEMENT
search = driver.find_element_by_name('s')

#-----------------FILL IN FORM 
search.send_keys('test')
search.send_keys(Keys.RETURN)

# PRINT SOURCE
print(driver.page_source)


#-----------------SLEEP
#time.sleep(2)


driver.quit()
