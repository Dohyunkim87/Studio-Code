import requests
from bs4 import BeautifulSoup

# 사람인 척 하기 위해 속이는 코드
header_user = {"User-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"}
# 탐색을 원하는 url
url = "https://naver.com"
# 탐색을 원하는 사이트의 데이터를 달라고 요청
req = requests.get(url, headers=header_user)

