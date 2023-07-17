import time
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime as dt
from pprint import pprint

chrome_driver_path = r"C:\Users\User\Desktop\Devellopement\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://jklm.fun/FQAU")

username = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[2]/input')
username.send_keys("KKPython")

submit = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[2]/button')
submit.click()

ended = False
while not ended:
    if keyboard.read_key('w'):
        letters_text = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div')
        letters = letters_text.text
        print(letters)

input()


