from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
chrome_driver = "CHROME_DRIVER_PATH"
login_url = "https://www.instagram.com/accounts/login/"
similar_account = "accoount_name"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get(login_url)
        time.sleep(2)
        username_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(USERNAME)
        pass_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_field.send_keys(PASSWORD)
        pass_field.send_keys(Keys.ENTER)
        time.sleep(3)
        not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(3)
        not_now = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now.click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/bikersofinstagram/{similar_account}")
        time.sleep(2)

        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)

        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_but = self.driver.find_elements_by_css_selector('li button')
        for but in all_but:
            try:
                but.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(chrome_driver)
bot.login()
bot.find_followers()
bot.follow()
