import os
import time
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv("../../.env")  # .env file

# -------------------- Constants -------------------- #
INSTAGRAM_URL = "https://instagram.com"
SIMILAR_ACCOUNT_USERNAME = "chefsteps"
INSTAGRAM_USERNAME = os.getenv("IG_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("IG_PASSWORD")
CHROME_OPTIONS = Options()
CHROME_SERVICE = Service()


# -------------------- Instagram Bot -------------------- #
class InstagramFollowerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=CHROME_OPTIONS, service=CHROME_SERVICE)
        self.driver.maximize_window()  # makes selenium full screen
        self.wait = WebDriverWait(self.driver, 5)  # option to wait while finding elements
        self.follow_buttons = None

    def login(self):
        self.driver.get(INSTAGRAM_URL)

        username_entry = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input._aa4b")))
        username_entry.click()
        username_entry.send_keys(INSTAGRAM_USERNAME)

        password_entry = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_entry.click()
        password_entry.send_keys(INSTAGRAM_PASSWORD)

        login_button = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
        login_button.click()

        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"{INSTAGRAM_URL}/{SIMILAR_ACCOUNT_USERNAME}")

        followers_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/chefsteps/followers/']")))
        followers_link.click()
        time.sleep(3)

        modal = self.driver.find_element(by=By.XPATH,
                                         value="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        for _ in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            self.follow()
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="button._acan")
        for button in follow_buttons[1:]:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9--")))
                cancel_button.click()
            else:
                time.sleep(2)

        # Clear the follow_buttons list after the loop ends
        follow_buttons = []

