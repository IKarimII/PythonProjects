import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime as dt
from pprint import pprint

chrome_driver_path = r"C:\Users\User\Desktop\Devellopement\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3590341680&f_AL=true&f_WT=2&geoId=102257491&keywords=python%20developer&location=Lebanon")

login = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login.click()

email_input = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
email_input.send_keys("karimhawwa@gmail.com")

password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys("Karimos@1432")

enter = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
enter.click()

jobs = driver.find_elements(By.CSS_SELECTOR, 'li div div div div a')
save = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')

for job in jobs:
    job.click()
    time.sleep(1)
    save.click()






