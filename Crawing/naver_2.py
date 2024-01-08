import requests
from bs4 import BeautifulSoup

# 사이트에 있는 네트워크 -> user-agent의 것을 긁어서 이렇게 만들어서 사람이 하는 것 처럼 착각하게 만든다
# 헤더 유저에 유저 에이전트 정보를 속인다. 없이 하면 파이썬3로 보내는 걸 바로 알 수 있기 때문에
# 1차적으로 덜 튕기는 것을 바라는 것이 목표

header_user = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}
# Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36
url = "https://naver.com"

req = requests.get(url, headers=header_user) # type: ignore
# print(req.request.headers)
print(dir(req)) # dir 명령어로 사용할 수 있는 것들을 확인할 수 있다

# 사이트를 크롤링 하기 위해서는 태그, 위치, 여러가지를 잘 이해해야 한다.