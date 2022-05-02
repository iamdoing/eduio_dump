# coding: utf-8
# author: du
# date: 2022-5-1

import os
import pickle
import time
import random

def log_in(driver, email, passwd, dump_cookie=True, resume=True):
    driver.get('https://www.educative.io/')
    time.sleep(10)
    if (not resume) or (not os.path.exists('cookies.pkl')):
        print('Start to Login via account and passwd')
        driver.find_element_by_xpath('//button[text()="Log In"]').click()
        time.sleep(3)
        driver.find_element_by_name("email").send_keys(email)
        time.sleep(2+random.random())
        driver.find_element_by_name("password").send_keys(passwd)
        time.sleep(2+random.random())
        driver.find_element_by_xpath('//button[text()="Log In"]').click()
        time.sleep(5+random.random())
        if dump_cookie:
            pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
    else:
        print('Will not Login again and juse use cookie')
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
    return driver


