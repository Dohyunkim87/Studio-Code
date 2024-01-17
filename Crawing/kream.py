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

for i in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    driver.save_screenshot("/Users/dohyunkim/Studio-Code/Crawing/kream_img/lv"+str(i)+".png")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

num = 1
for i in items:
    product_name = i.select_one(".translated_name")

    if "알마" in product_name.text:
        product_brand = i.select_one(".product_info_brand.brand")
        product_name_hood = i.select_one(".translated_name")
        product_price = i.select_one(".amount")

        print(f"[{num}]")
        print(f"브랜드 : {product_brand.text}")
        print(f"제품명 : {product_name_hood.text}")
        print(f"가 격 : {product_price.text}")
        print()

        num +=1
driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.HOME)
# driver.find_element(By.CSS_SELECTOR, ".btn_search_delete").click()
driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click()
time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, ".btn_cancle").click()

driver.quit() # 최종적으로 이 것을 입력해서 종료하도록 한다. (크롤링이 끝나면)