from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

options = Options()
service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get(url=URL)

count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text

print(count)

driver.quit()
