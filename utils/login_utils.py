# coding: utf-8
# author: du
# date: 2022-5-1

import os
import pickle


def log_in(driver, email, passwd, dump_cookie=True, resume=True):
    if (not resume) or (not os.path.exists('cookies.pkl')):
        driver.find_element_by_xpath('//button[text()="Log In"]').click()
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_xpath('//button[text()="Log In"]').click()
        if dump_cookie:
            pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
    else:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
    return driver

