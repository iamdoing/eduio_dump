
import json
from selenium import webdriver

import cfg

def gen_print_driver():
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
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=cfg.CHROMEDRIVER_PATH)
    return driver
