from selenium import webdriver
import os
import shutil
import time

opt = webdriver.ChromeOptions()
opt.add_extension("metamask.crx")

driver = webdriver.Chrome("chromedriver", chrome_options=opt)
time.sleep(5)
createurl = "https://opensea.io/collection/we-are-frogs/assets/create"


prefix = "I am Frog #"
driver.switch_to.window(driver.window_handles[0])
button = driver.find_element_by_tag_name("button")
button.click()
time.sleep(1)

button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')
button.click()
time.sleep(1)


button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]')
button.click()
time.sleep(1)

field = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input')

temp = open("secretKey")
field.send_keys(temp.read())
temp.close()

id = driver.find_element_by_id("password")
id.send_keys("djfudnj1")

ps = driver.find_element_by_id("confirm-password")
ps.send_keys("djfudnj1")

checkbox = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div')
checkbox.click()

button = driver.find_element_by_tag_name("button")
button.click()
time.sleep(3)

button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/button')
button.click()
time.sleep(1)

driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.get("https://opensea.io")
time.sleep(2)

idbutton = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/nav/ul/div[2]/div/li/a/i')
idbutton.click()
time.sleep(2)

metamaskbutton = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li[1]/button/div[2]/span')
metamaskbutton.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1])

button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]')
button.click()
time.sleep(2)

button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
button.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[0])

time.sleep(5)

files = os.listdir()

for i, el in enumerate(files):
    if not el.endswith(".png"):
        continue
    filename = prefix + str(1 + i)
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
            close = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button/i')
            close.click()
            break
        except:
            time.sleep(1)
    
    time.sleep(1)
    sellButton = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a')
    sellButton.click()
    time.sleep(1)
    priceField = driver.find_element_by_name("price")
    priceField.send_keys("0.001")
    time.sleep(2)
    listingButton = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[4]/button')
    listingButton.click()
    while (1):
        try:
            close = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/section/div/div/section/div/div/div/div/div/div/div/button')
            close.click()
            break
        except:
            time.sleep(1)
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    sign = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
    sign.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    while (1):
        try:
            close = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button/i')
            close.click()
            break
        except:
            time.sleep(1)

    shutil.move(el, "uploaded/" + el)
    time.sleep(2)
