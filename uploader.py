from selenium import Webdriver
import os
import shutil
import time

opt = Webdriver.ChromeOptions()
opt.add_extensioin("metamask.crx")

driver = Webdriver.Chrome("chromedriver", chrome_options=opt)
createurl = "https://opensea.io/collection/wearefrogs/assets/create?locale=ko"

files = os.listdir()

prefix = "I am Frog #"


for i, el in enumerate(files):
    if not el.endswith(".png"):
        continue

    driver.get(createurl)
    time.sleep(3)
    uploader = driver.find_element_by_id("media")
    uploader.send_keys("/Users/bhban/Desktop/pxls/" + el)
    time.sleep(2)
    nameField = driver.find_element_by_id("name")
    nameField.send_keys(filename)
    time.sleep(1)
    descriptionField = driver.find_element_by_id("description")
    descriptionField.send_keys(filename)
    time.sleep(1)
    button = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button')
    button.click()

    while (1):
        try:
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button/i')
            break
        except:
            time.sleep(1)
    shutil.move(el, "uploaded/" + el)
    time.sleep(1)
