from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 사람인 척 하기 위해 속이는 코드
header_user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"}

# 기본 url에 키워드까지 입력 가능하도록 변경
base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
key_word = input("검색어를 입력해주세요 :")

# 탐색을 원하는 url
url = base_url + key_word
# 탐색을 원하는 사이트의 데이터를 달라고 요청
driver = webdriver.Chrome()
driver.get(url)
# time.sleep(4)

for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

total_area = soup.select(".view_wrap")
#.bx.type_ad
if total_area:
    areas = total_area
else:
    print(total_area)
    print("클래스 변경 필요")

# 스크롤 실행 코드
# driver.execute_script("window.scrollTo(0, 10000)") # 좌표 입력방식이라 안먹음!
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 뷰탭기준을 하기 때문에, 실제로 스크롤이 밑으로 내려가야한다

rank_num = 1
for i in areas: # type: ignore
    ad = i.select_one(".link_ad")
    if ad:
        continue

    print(f"[{rank_num}]")
    title = i.select_one(".title_link._cross_trigger")
    name = i.select_one(".name")
    print(f'제목 : {title.text}')
    print(f'작성자 : {name.text}')
    print(f'링크 : {title['href']}')
    print()

    rank_num += 1
