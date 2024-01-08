import requests
from bs4 import BeautifulSoup

# 사람인 척 하기 위해 속이는 코드
header_user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"}

#기본 url에 키워드까지 입력 가능하도록 변경
base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
key_word = input("검색어를 입력해주세요 :")

# 탐색을 원하는 url
url = base_url + key_word
# 탐색을 원하는 사이트의 데이터를 달라고 요청
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# print(soup)

#title_link _cross_trigger : 글의 제목
#name : 작성자

title = soup.select(".title_link._cross_trigger") # 띄워쓰기로 구분된 2가지의 클래스를 . 으로 구분
name = soup.select(".name")

# print(type(name))
# print(list(name))

for i in zip(title, name):
    print(f'제목 : {i[0].text}')
    print(f'작성자 : {i[1].text}')
    print(f'링크 : {i[0]["href"]}')
    print()