import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

# get 방식 : 서버에게 리소스를(자원) 보내도록 요청, 데이터를 수신하는 기능
req = requests.get(url)
html = req.text
# print(html)

soup = BeautifulSoup(html, "html.parser")
query = soup.select_one(".ContentHeaderView-module__tab___uYoNi type_news")
print(query)