import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





def flipkart_auto():
    global driver
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.flipkart.com/')
    if not elementPresent('_2zrpKA'):
        exit()
    search_box = driver.find_element_by_class_name('_2zrpKA')
    search_box.send_keys(os.environ['FlipUser'])
    search_box = driver .find_element_by_xpath('//input[@type="password"]')
    search_box.send_keys(os.environ['FlipPass'])
    driver.find_element_by_class_name('_1avdGP').click()
    if not elementPresent('O8ZS_U'):
        exit()
    time.sleep(2)
    search_box = driver.find_element_by_class_name('O8ZS_U')
    search_box = driver.find_element_by_xpath('//input[@title="Search for products, brands and more"]')
    # search_box.send_keys('Iphone pro')
    search_box.send_keys('google home')
    search_box.send_keys(Keys.ENTER)
    if not elementPresent('_31qSD5'):
        exit()
    link = driver.find_element_by_class_name('_31qSD5').get_attribute('href')
    time.sleep(2)
    driver.execute_script("window.open('');")
    # Switch to the new window and open URL B
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    if not elementPresent('_2AkmmA'):
        exit()

    driver.find_element_by_class_name('_3X4tVa').send_keys('5600S85')
    driver.find_element_by_class_name('_2aK_gu').click()
    time.sleep(1)
    buyNow = driver.find_element_by_class_name('_2kuvG8')

    if buyNow.is_enabled():
       driver.find_element_by_class_name('_2kuvG8').click()
       if not elementPresent('_2Q4i61'):
           exit()
       else:
           driver.find_element_by_class_name('_2Q4i61').click()
    else :
        print('Item Out of Stock')
        driver.quit()

def elementPresent(className):
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, className))
        WebDriverWait(driver, 8).until(element_present)
        return 1
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
        return 0


#start of the program
if __name__ == "__main__":
    flipkart_auto()

