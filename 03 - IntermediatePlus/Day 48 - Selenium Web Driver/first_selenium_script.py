from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
service = Service()

driver = webdriver.Chrome(options=options, service=service)  # driver object

driver.get("https://amazon.com.tr")

# We can find elements by; id,classname, name attribute, css selector, and more.
# Check Selenium Documentation https://www.selenium.dev/documentation/
# Learn about XPath : https://www.tutorialspoint.com/xpath/index.htm

# driver.close()  # closes a single tab
driver.quit()  # close the entire program
