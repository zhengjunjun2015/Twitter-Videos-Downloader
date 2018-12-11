# -*- encoding UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
    
class upload_topbuzz:
    def acsess_browser(url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(5)
        return driver
    
    def login(driver):
        xpaths = {
                'a_tag' : '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div[3]/div/div[3]/div/div[3]/a[1]',
                'google_login_botton' : '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div[3]/div/div[3]/div/div[1]/div[3]',
                'google_login_mail' : '//*[@id="identifierId"]',
                'google_login_pass' : '//*[@id="password"]/div[1]/div/div[1]/input',
                } 
    
        username = '10380r'
        password = 'r19971104'
    
        google_login_botton = driver.find_element_by_xpath(xpaths['google_login_botton'])
        google_login_botton.click()
        google_input_email = driver.find_element_by_xpath(xpaths['google_login_mail'])
        google_input_email.send_keys(username, Keys.ENTER)
        driver.implicitly_wait(3)
        google_input_password = driver.find_element_by_xpath(xpaths['google_login_pass'])
        google_input_password.send_keys(password, Keys.ENTER)
   
    def upload(driver):
        xpaths = {
                'a_tag' : '//*[@id="root"]/div/div[1]/div[1]/div[2]/div/span/a',
                }

    def main():
        url = 'https://www.topbuzz.com/'
        driver = acsess_browser(url)
        login(driver)
        time.sleep(10000000000)

        
    if __name__ == '__main__':
        main()
