#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as seleniumException
import json
import sys

########################## AUXILIARY ###########################
# Create the asked selenium webdriver by name
class Drivers:
    def firefox(self):
        return webdriver.Firefox()

    def chrome(self):
        return webdriver.Chrome()

    def getDriver(self, name):
        return getattr(self, name)()

def claimReward(driver, cookies):
    driver.get(dci_url)
    #remove pop-up
    close_button = "components-home-assets-__sign-guide_---guide-close---2VvmzE"
    pop_up = driver.find_element(By.CLASS_NAME, close_button)
    pop_up.click()

    # Load cookies
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    # Click on reward
    claimable = "components-home-assets-__sign-content_---sign-wrapper---38rWqB"
    reward = driver.find_element(By.CLASS_NAME, claimable)
    reward.click()

############################ VARIABLES #############################
# Fetch Arguments
args = sys.argv
driver_type = args[1]
coockies_file = args[2]

# Process Arguments
driver = Drivers().getDriver(driver_type)
cookies = json.load(open(coockies_file, "rb"))

# DAILY CHECK-IN URL:
dci_url = "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&mhy_auth_required=true&mhy_presentation_style=fullscreen&lang=en-us&bbs_theme=dark&bbs_theme_device=1"

############################## MAIN ###############################
try:
    claimReward(driver, cookies)
except seleniumException.NoSuchElementException:
    print("No rewards available to claim.")
finally:
    driver.quit()
