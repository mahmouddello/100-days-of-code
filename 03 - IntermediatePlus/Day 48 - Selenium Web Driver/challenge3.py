from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://secure-retreat-92358.herokuapp.com/"

options = Options()
service = Service()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)

driver.get(URL)

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

f_name.send_keys("Mahmoud")
l_name.send_keys("Dello")
email.send_keys("mahmoddello68@gmail.com")

send_button = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
send_button.click()
