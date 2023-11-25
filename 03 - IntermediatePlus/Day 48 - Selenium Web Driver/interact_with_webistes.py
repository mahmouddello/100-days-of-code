from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

options = Options()
service = Service()

options.add_experimental_option("detach", True)

# driver1 = webdriver.Chrome(service=service, options=options)
driver2 = webdriver.Chrome(service=service, options=options)

# driver1.get(URL)

# # Click a hyperlink or a button in the page:
# # 1 - Select the element
# # 2 - element.click()
# article_count = driver1.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

driver2.get(URL)
driver2.maximize_window()
search = driver2.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
