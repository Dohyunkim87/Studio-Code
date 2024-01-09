import requests
from bs4 import BeautifulSoup

# song_num_text = "javascript:melon.link.goAlbumDetail('111352904')"

def get_nums(song_num_text):
    song_num = []
    for num in song_num_text:
        if num.indigit(): # 10진수로 전환
            song_num.append(num)
        song_num = "".join(song_num) #결과값 확인
        return song_num


header_user = {"User-Agent":"Mozilla/5.0"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

lst_all = lst50 + lst100
for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 a")
    singer_link = get_nums(singer("href"))
    album = i.select_one(".ellipsis.rank03 a")
    album_link = get_nums(album("href"))
    print(f'순위 ; [{rank}]')
    print(f'제목 : {title.text}')
    print(f'가수 : {singer.text}')
    print(f'가수링크 : https://www.melon.com/artist/timeline.html?artistId={singer_link}')
    print(f'앨범 : {album.text}')
    print(f'앨범링크 : https://www.melon.com/album/detail.htm?albumId={album_link}')
    print()