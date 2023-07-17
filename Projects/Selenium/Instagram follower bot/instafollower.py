import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\User\Desktop\Devellopement\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


class InstaFollower():
    def __init__(self):
        self.username = 'CookingwithPython'
        self.password = '7Ui;Md75W!v#M28'

    def login(self):
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(self.username)
        time.sleep(0.5)
        password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.password)
        time.sleep(0.5)
        login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Home"]')))
        driver.get('https://www.instagram.com/chefsteps/')
        self.follow()

    def follow(self):
        time.sleep(4)
        followers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                    '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')))
        followers.click()
        follow_buttons = driver.find_elements(By.CSS_SELECTOR, 'div div div div div div button')
        time.sleep(2)
        modal = driver.find_element(By.CLASS_NAME, '_aano')
        ended = False
        time.sleep(2)
        while not ended:
            for button in follow_buttons:
                print(button.text)
                try:
                    button.click()
                except:
                    print('failed')
                    pass
                time.sleep(1)
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            follow_buttons = driver.find_elements(By.CSS_SELECTOR, 'div div div div div div button')

