from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys   # 키보드 입력 같은 어떠한 동작을 할 때
from selenium.webdriver.common.by import By       # 클래스, 아이디, css_selector을 이요할 때
from bs4 import BeautifulSoup
import time
from selenium.webdriver import ActionChains

user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"

options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://m2.melon.com/index.htm"
driver.get(url)

time.sleep(0.5)
if driver.current_url != url:
    driver.get(url)

driver.find_element(By.LINK_TEXT, "멜론차트").click() # A 태그를 활용하여 홈페이지의 하이퍼 링크를 식별한다.
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".swiper_slide.main_chart #moreBtn").click() #상위태그의 클래스 + 하위태그(버튼)의 아이디
#moreBtn중에서 1번쨰
#driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(1)

melon_chart = driver.find_element(By.CSS_SELECTOR, '#_chartList')
list_100 = melon_chart.find_elements(By.CSS_SELECTOR, '.list_item')
time.sleep(1)

action = ActionChains

for i in list_100:
    title = i.find_element(By.CSS_SELECTOR, ".title.ellipsis")
    singer = i.find_element(By.CSS_SELECTOR, ".name.ellipsis")

    action.move_to_element(i).perform()
    i.find_element(By.CSS_SELECTOR, ".inner > span").click()
    time.sleep(0.5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    driver.back()
    print(title.text)
    print(singer.text)
    print()