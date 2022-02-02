from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# convert strings like "80.1 million" to its equivalent integer (80100000)


def GetCookieCount():
    var = cookie_count.text
    var = var.split("\n")[0]
    var = var.replace(" cookies", "")
    var = var.replace(" cookie", "")
    return int(ConvertToInt(var))


def ConvertToInt(cookie_count):
    value = 0
    if 'million' in cookie_count:
        value = int(float(cookie_count.split()[0]) * 10**6)
    elif 'billion' in cookie_count:
        value = int(float(cookie_count.split()[0]) * 10**9)
    elif 'trillion' in cookie_count:
        value = int(float(cookie_count.split()[0]) * 10**12)
    elif 'quadrillion' in cookie_count:
        value = int(float(cookie_count.split()[0]) * 10**15)
    elif 'quintillion' in cookie_count:
        value = int(float(cookie_count.split()[0]) * 10**18)
    elif 'sextillion' in cookie_count:
        value = int(float(cookie_count.split()[0]) * 10**21)
    elif ',' in cookie_count:
        value = int(cookie_count.replace(',', ''))
    else:
        value = cookie_count

    return value


# python -m pipenv run python cookieclicker.py
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")


actions = ActionChains(driver)
actions.click(cookie)
actions.click(cookie)


for i in range(5000):
    actions.click(cookie)
    actions.perform()

    print(GetCookieCount())

    try:
        upgrades = [driver.find_element(By.ID, "upgrade" + str(i))
                    for i in range(0, -1, -1)]
        for upgrade in upgrades:
            classname = upgrade.get_attribute("class")
            print(classname)
            if classname == "crate upgrade enabled":
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(upgrade)
                upgrade_actions.click()
                upgrade_actions.perform()
    except:
        print("no upgrades found")

    try:
        items = [driver.find_element(By.ID, "productPrice" + str(i))
                 for i in range(10, -1, -1)]

        for item in items:
            if(item.text != ""):
                value = int(ConvertToInt(item.text))
                if value <= GetCookieCount():
                    upgrade_actions = ActionChains(driver)
                    upgrade_actions.move_to_element(item)
                    upgrade_actions.click()
                    upgrade_actions.perform()
    except:
        print("something went wrong with items")
