import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3641418488&f_AL=true&geoId=101165590&keywords=python%20developer&location=United%20Kingdom&refresh=true"

options = Options()
service = Service()

browser = webdriver.Chrome(options=options, service=service)

browser.get(url=URL)

browser.maximize_window()

sign_in_button1 = browser.find_element(By.CSS_SELECTOR,
                                       "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button1.click()

email_input = browser.find_element(By.CSS_SELECTOR, "#username")
password_input = browser.find_element(By.CSS_SELECTOR, "#password")

email_input.send_keys("your-email")
password_input.send_keys("your-password")

sign_in_button2 = browser.find_element(By.CSS_SELECTOR,
                                       "#organic-div > form > div.login__form_action_container > button")
sign_in_button2.click()

time.sleep(10)

listings = browser.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
print(len(listings))

for job in listings:
    browser.execute_script("arguments[0].scrollIntoView();", job)
    job.click()
    time.sleep(3)
    save = browser.find_element(By.CLASS_NAME, "jobs-save-button")
    save.click()
    time.sleep(2)

time.sleep(60)
browser.quit()
