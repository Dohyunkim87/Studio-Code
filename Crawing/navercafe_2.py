from selenium import webdriver
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"}

url = "https://section.cafe.naver.com/ca-fe/home"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

total_area1 = soup.select("a.item")
total_area2 = soup.select(".editors_pick .popular_items")

if total_area1:
    areas1 = total_area1
    areas2 = total_area2
else:
    print("해당 클래스를 가진 요소가 없습니다.")
    areas1 = []
    areas2 = []

print("인기글 베스트")
for i in areas1:
    title = i.select_one(".tit")
    name = i.select_one(".cafe_name")
    print(f'제목 : {title.text}')
    print(f'작성자 : {name.text}')
    print()

print("인기글 및 이웃인기글")
for i in areas2:
    title = i.select_one(".tit")
    name = i.select_one(".cafe_name")
    print(f'제목 : {title.text}')
    print(f'작성자 : {name.text}')
    print()
