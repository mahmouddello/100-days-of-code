from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.python.org")

dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
dates = [date.text for date in dates]

events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = [event.text for event in events]


calendar = {}
calendar2 = {i: {"time": dates[i], "date": events[i]} for i in range(len(dates))}

for index in range(len(dates)):
    calendar[index] = {
        "time": dates[index],
        "name": events[index]
    }


print(calendar)
print(calendar2)

driver.quit()
