from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime as dt
from pprint import pprint
chrome_driver_path = r"C:\Users\User\Desktop\Devellopement\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.Python.org")
up_coming_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_links = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')


events = [{f"{dt.datetime.now().year}-{up_coming_events[n].text}":event_links[n].text} for n in range(len(up_coming_events))]
pprint(events)