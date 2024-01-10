import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0"}
# 유저 정보 중요함, 반응형 창으로 인해 오류가 발생한 것으로 확인됨. 꼭 주의할 것

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")
# print(soup)

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
# print(lst50)

# rank_num = 1
# for i in lst50:
#     print(f"[{rank_num}]")
#     title = i.select_one(".ellipsis.rank01 a")
#     singer = i.select_one(".ellipsis.rank02 a")
#     album = i.select_one(".ellipsis.rank03 a")
#     print(f'제목 : {title.text}')
#     print(f'가수 : {singer.text}')
#     print(f'앨범 : {album.text}')
#     print()

#     rank_num += 1

# for i in lst100:
#     print(f"[{rank_num}]")
#     title = i.select_one(".ellipsis.rank01 a")
#     singer = i.select_one(".ellipsis.rank02 a")
#     album = i.select_one(".ellipsis.rank03 a")
#     print(f'제목 : {title.text}')
#     print(f'가수 : {singer.text}')
#     print(f'앨범 : {album.text}')
#     print()

#     rank_num += 1

# for rank, i in enumerate(lst50, 1):
#     print(f"[{rank}]")
#     title = i.select_one(".ellipsis.rank01 a")
#     singer = i.select_one(".ellipsis.rank02 a")
#     album = i.select_one(".ellipsis.rank03 a")
#     print(f'제목 : {title.text}')
#     print(f'가수 : {singer.text}')
#     print(f'앨범 : {album.text}')
#     print()

# for rank, i in enumerate(lst100, 51):
#     print(f"[{rank}]")
#     title = i.select_one(".ellipsis.rank01 a")
#     singer = i.select_one(".ellipsis.rank02 a")
#     album = i.select_one(".ellipsis.rank03 a")
#     print(f'제목 : {title.text}')
#     print(f'가수 : {singer.text}')
#     print(f'앨범 : {album.text}')
#     print()

lst_all = lst50 + lst100
for rank, i in enumerate(lst_all, 1):
    print(f"[{rank}]")
    title = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")
    print(f'제목 : {title.text}')
    print(f'가수 : {singer.text}')
    print(f'앨범 : {album.text}')
    print()