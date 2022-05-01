# coding: utf-8
# author: du
# date: 2022-5-1

import random
import time

import cfg
from utils import driver_utils, login_utils


def recurse_dump_from_1st(first_page_url, driver):
    driver.get(first_page_url)
    time.sleep(5 + random.randint(0, 10))
    driver.execute_script('window.print();')
    while True:
        try:
            time.sleep(5 + random.randint(0, 10))
            driver.find_element_by_xpath('//button[text()="Next"]').click()
            time.sleep(5 + random.randint(10, 16))
            driver.execute_script('window.print();')
        except:
            print('Finished, if not, start from current page and run again')
            break
    driver.quit()


def main(args=None):
    first_page_url = 'https://www.educative.io/courses/distributed-systems-practitioners/R8XGr1R1qRz'
    driver = driver_utils.gen_print_driver()
    driver = login_utils.log_in(driver, cfg.email, cfg.passwd, dump_cookie=True, resume=True)
    recurse_dump_from_1st(first_page_url, driver)


if __name__ == '__main__':
    main()
