# coding: utf-8
# author: du
# date: 2022-5-1


from selenium import webdriver
import json
import sys
import pickle
import time
import random

sys.path.insert(0, 'd:\\code\\edu_io_crawl')


chrome_options = webdriver.ChromeOptions()
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
# chrome_options.add_argument(r"--user-data-dir=C:\Users\du\AppData\Local\Google\Chrome\User' 'Data\Default\Login' 'Data")
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='../chromedriver.exe')
# cooki = 'g_state={"i_p":1651403110798,"i_l":1}; _gcl_au=1.1.1543557046.1651395946; usprivacy=1---; hubspotutk=7d85b001a849cd3316b1ee9145e90815; __hssrc=1; logged_in=; OneTrustWPCCPAGoogleOptOut=false; _hjSessionUser_1142875=eyJpZCI6ImNlNjFmNGUxLTBmNDQtNWI5MS04ZTExLThhZWVjNTIzYTk2NiIsImNyZWF0ZWQiOjE2NTEzOTU5NTI2NzcsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1142875=eyJpZCI6ImFjNDkzMzU2LWVkNmYtNDkyZS1iMmZlLWFiZjAzNjYxYzkzZSIsImNyZWF0ZWQiOjE2NTEzOTg1MzA2MTksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; __hstc=10449898.7d85b001a849cd3316b1ee9145e90815.1651395955181.1651395955181.1651398532604.2; OptanonConsent=isIABGlobal=false&datestamp=Sun+May+01+2022+17%3A56%3A12+GMT%2B0800+(Hong+Kong+Standard+Time)&version=6.32.0&hosts=&consentId=c30a5a66-32e1-44dc-8cbe-c7460c583d33&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BBJ&AwaitingReconsent=false; OptanonAlertBoxClosed=2022-05-01T09:56:12.262Z; __hssc=10449898.2.1651398532604; _dd_s=logs=1&id=fbd9507e-5491-43de-bc72-9328909c9e3b&created=1651395902360&expire=1651399970326'
# driver.add_cookie(json.loads(cooki))
driver.get("https://www.educative.io/")
driver.find_element_by_xpath('//button[text()="Log In"]').click()
driver.find_element_by_name("email").send_keys("")
driver.find_element_by_name("password").send_keys("")
driver.find_element_by_xpath('//button[text()="Log In"]').click()
pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))


cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

first_page_url = "https://www.educative.io/courses/distributed-systems-practitioners/R8XGr1R1qRz"
first_page_url = "https://www.educative.io/courses/distributed-systems-practitioners/YV6ZyYLZomA"
driver.get(first_page_url)
time.sleep(20)
driver.execute_script('window.print();')
while True:
    try:
        time.sleep(5+random.randint(0, 10))
        driver.find_element_by_xpath('//button[text()="Next"]').click()
        time.sleep(5+random.randint(10, 16))
        driver.execute_script('window.print();')
    except:
        print('Finished')
        break
driver.quit()
