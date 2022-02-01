from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)

search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


# wait untill a element with id "main" is present on the page

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except:
    print("TIMEOUT ERROR: element was not found within time")
    driver.quit()

finally:
    print("main found!")


print(main.text)
print("-------------------------")

articles = main.find_elements(By.TAG_NAME, "article")
for article in articles:
    header = article.find_element(By.CLASS_NAME, "entry-summary")
    print(header.text)


# print(driver.page_source)

time.sleep(5)

driver.quit()
