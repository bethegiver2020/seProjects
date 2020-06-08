from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import multiprocessing
import os


def flipkart_auto(searchItem):
    global driver
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.flipkart.com/')
    if not elementPresent('_2zrpKA'):
        exit()
    search_box = driver.find_element_by_class_name('_2zrpKA')
    search_box.send_keys('7795745074')
    search_box = driver .find_element_by_xpath('//input[@type="password"]')
    search_box.send_keys('rangasiri@123')
    driver.find_element_by_class_name('_1avdGP').click()
    # time.sleep(5)
    if not elementPresent('O8ZS_U'):
        exit()
    time.sleep(2)
    search_box = driver.find_element_by_class_name('O8ZS_U')
    search_box = driver.find_element_by_xpath('//input[@title="Search for products, brands and more"]')
    # search_box.send_keys('Iphone pro')
    search_box.send_keys(searchItem)
    search_box.send_keys(Keys.ENTER)
    if not elementPresent('_31qSD5'):
        exit()
    link = driver.find_element_by_class_name('_31qSD5').get_attribute('href')
    #driver.find_element_by_class_name('_31qSD5').click()
    #time.sleep(4)
    time.sleep(2)
    driver.execute_script("window.open('');")
    # Switch to the new window and open URL B
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    if not elementPresent('_2AkmmA'):
        exit()
    buyNow = driver.find_element_by_class_name('_2AkmmA')

    if buyNow.is_enabled():
       driver.find_element_by_class_name('_2AkmmA').click()
    else :
        print('Item Out of Stock')
        # driver.quit()
    # driver.find_element_by_css_selector('._2AkmmA._3-iCOr.wvj5kH').click()
    # time.sleep(2)
    # driver.find_element_by_class_name('_3qjVwf').click()

    # try:
    #     time.sleep(5)
    #    # driver.find_element_by_class_name('_3uuwnI').click()
    #     driver.find_element_by_css_selector('._2AkmmA._3-iCOr.wvj5kH').click()
    #     time.sleep(2)
    #     driver.find_element_by_class_name('_3qjVwf').click()
    # except Exception as e:
    #     print(e)
    #     #driver.find_element_by_class_name('_3-iCOr').click()
    # print(link)
    # time.sleep(5)
    #driver.get('https://www.flipkart.com/poco-f1-graphite-black-64-gb/p/itmf8fyjyssnt25c?pid=MOBF85V7A6PXETAX&srno=s_1_1&otracker=AS_QueryStore_OrganicAutosuggest_1_4&lid=LSTMOBF85V7A6PXETAXH9JSSB&fm=SEARCH&iid=4883686e-e210-49e9-a67c-3f727d9d39b6.MOBF85V7A6PXETAX.SEARCH&ppt=Homepage&ppn=Homepage&ssid=fd7n9f4sj40000001535366377426&qH=f6f38324df02133a')
    #give poco f1 mobile page link below
    #https://www.flipkart.com/poco-f1-graphite-black-64-gb/p/itmf8fyjyssnt25c?pid=MOBF85V7A6PXETAX&srno=s_1_1&otracker=AS_QueryStore_OrganicAutosuggest_1_4&lid=LSTMOBF85V7A6PXETAXH9JSSB&fm=SEARCH&iid=4883686e-e210-49e9-a67c-3f727d9d39b6.MOBF85V7A6PXETAX.SEARCH&ppt=Homepage&ppn=Homepage&ssid=fd7n9f4sj40000001535366377426&qH=f6f38324df02133a
    #driver.get('https://www.flipkart.com/poco-f1-graphite-black-64-gb/p/itmf8fyjyssnt25c?pid=MOBF85V7A6PXETAX&srno=s_1_1&otracker=AS_QueryStore_OrganicAutosuggest_1_4&lid=LSTMOBF85V7A6PXETAXH9JSSB&fm=SEARCH&iid=4883686e-e210-49e9-a67c-3f727d9d39b6.MOBF85V7A6PXETAX.SEARCH&ppt=Homepage&ppn=Homepage&ssid=fd7n9f4sj40000001535366377426&qH=f6f38324df02133a')
    #driver.find_element_by_xpath('//button[@type="button"]').click()
    #print(driver.find_element_by_xpath('//img[@src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/flipkart-plus_4ee2f9.png"]').text)

    #driver.quit()

def elementPresent(className):
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, className))
        WebDriverWait(driver, 8).until(element_present)
        return 1
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
        return 0



if __name__ == "__main__":
    # printing main program process id
    print("ID of main process: {}".format(os.getpid()))

    # creating processes
    p1 = multiprocessing.Process(target=flipkart_auto,args=('Iphone Pro',))
    p2 = multiprocessing.Process(target=flipkart_auto,args=('Samsung note 10',))
    p3 = multiprocessing.Process(target=flipkart_auto,args=('Apple watch',))
    p4 = multiprocessing.Process(target=flipkart_auto,args=('google home',))

    # starting processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until processes are finished
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    # both processes finished
    print("Both processes finished execution!")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
    print("Process p3 is alive: {}".format(p3.is_alive()))
    print("Process p4 is alive: {}".format(p4.is_alive()))
# flipkart_auto()

