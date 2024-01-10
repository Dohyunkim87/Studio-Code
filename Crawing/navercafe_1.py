from selenium import webdriver
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"}

url = "https://section.cafe.naver.com/ca-fe/home"
# base_url = "https://section.cafe.naver.com/ca-fe/home"
# key_word = input("검색어를 입력해주세요 :")

# 탐색을 원하는 url
# url = base_url + key_word
# 탐색을 원하는 사이트의 데이터를 달라고 요청
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

total_area1 = soup.select("a.item")

if total_area1:
    areas = total_area1
else:
    print("해당 클래스를 가진 요소가 없습니다.")
    areas = []

rank_num = 1
for i in areas: # type: ignore
    ad = i.select_one(".link_ad")
    if ad:
        continue

    print(f"[{rank_num}]")
    title = i.select_one(".item_list.tit")
    name = i.select_one(".item_list.cafe_name")
    print(f'제목 : {title.text}')
    print(f'작성자 : {name.text}')
    print(f'링크 : {title['href']}')
    print()

    rank_num += 1
  