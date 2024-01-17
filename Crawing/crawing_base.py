from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys   # 키보드 입력 같은 어떠한 동작을 할 때
from selenium.webdriver.common.by import By       # 클래스, 아이디, css_selector을 이요할 때
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"

options = Options()
options.add_argument(f"user-agents={user_agent}")
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = ""
driver.get(url)
