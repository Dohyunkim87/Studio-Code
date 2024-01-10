from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys   # 키보드 입력 같은 어떠한 동작을 할 때
from selenium.webdriver.common.by import By       # 클래스, 아이디, css_selector을 이요할 때
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0"


options = Options()
options.add_argument(f"user-agents={user_agent}")
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click()
time.sleep(1)

# input_search show_placeholder_on_focus : 클래스
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("루이비통")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

# driver.quit() # 최종적으로 이 것을 입력해서 종료하도록 한다. (크롤링이 끝나면)