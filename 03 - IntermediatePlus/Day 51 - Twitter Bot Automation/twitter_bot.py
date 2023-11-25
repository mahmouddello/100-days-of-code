import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv("../../.env")


class InternetSpeedTwitterBot:
    def __init__(self, upload, download):
        self.driver = self.initialize_driver()
        self.upload = upload
        self.download = download

    @staticmethod
    def initialize_driver():
        return webdriver.Chrome(options=Options(), service=Service())

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        test_speed_button = self.driver.find_element(By.CLASS_NAME, "start-button")
        test_speed_button.click()

        # Wait for an element that appears after the test is complete
        WebDriverWait(self.driver, 300).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "result-label"))
        )

        # Now that the test is complete, fetch the upload and download speeds
        self.upload = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        self.download = self.driver.find_element(By.CLASS_NAME, "download-speed").text

        self.driver.quit()  # close all tabs and quit the browser
        return float(self.upload), float(self.download)

    def twitter_login(self):
        signin_button = self.driver.find_element(By.CSS_SELECTOR, 'a[data-testid="loginButton"]')
        signin_button.click()

        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text")))

        username_input.send_keys(os.getenv("TWITTER_USERNAME"))

        next_button = self.driver.find_element(
            By.XPATH,
            "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]"
        )
        next_button.click()

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        password_input.send_keys(os.getenv("TWITTER_PASSWORD"))

        login_button = self.driver.find_element(
            By.XPATH,
            "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div["
            "1]/div/div/div"
        )
        login_button.click()

    def tweet_at_provider(self, promised_download, promised_upload, download, upload):
        self.driver = self.initialize_driver()
        self.driver.get("https://twitter.com")

        self.twitter_login()  # login with twitter credentials

        editor_container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "DraftEditor-editorContainer"))
        )
        editor_container.click()

        tweet_textbox = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')

        message = (f"Hey @TurkTelekom, why is my internet speed {download}down/{upload}up when I"
                   f" pay for {promised_download}down/{promised_upload}up?")

        tweet_textbox.send_keys(message)

        post_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')
        post_button.click()

        time.sleep(10)

        self.driver.quit()
