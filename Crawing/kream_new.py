from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0"

options = Options()
options.add_argument(f"user-agent={user_agent}")
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

brand_count = int(input("브랜드 입력 횟수를 설정하세요 (1부터 9까지 가능): "))
item_count = int(input("필터링할 아이템명 입력 횟수를 설정하세요 (1부터 9까지 가능): "))

result = []
num = 1

for _ in range(brand_count):
    brand = input("브랜드를 입력하세요: ")
    for _ in range(item_count):
        item_name = input("필터링할 아이템명을 입력하세요: ")

        search_input = driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus")
        search_input.clear()
        search_input.send_keys(item_name)
        time.sleep(1)

        search_input.send_keys(Keys.ENTER)
        time.sleep(1)

        for i in range(10):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        items = soup.select(".item_inner")

        for item in items:
            product_brand = item.select_one(".product_info_brand.brand")
            product_name_hood = item.select_one(".translated_name")
            product_price = item.select_one(".amount")

            if brand in product_brand.text and item_name in product_name_hood.text:
                result.append(f"[{num}]")
                result.append(f"브랜드: {product_brand.text}")
                result.append(f"제품명: {product_name_hood.text}")
                result.append(f"가격: {product_price.text}")
                result.append("")
                num += 1

if num == 1:
    result.append("검색 결과가 없습니다.")

with open("result.txt", "w") as file:
    file.write("\n".join(result))

driver.quit()
