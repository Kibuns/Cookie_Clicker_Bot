from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# python -m pipenv run python click.py
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')

try:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
    )
except:
    print("TIMEOUT ERROR: element was not found within time")
    driver.quit()

finally:
    print("link found!")
    link.click()


time.sleep(4)

driver.quit()
