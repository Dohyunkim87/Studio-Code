from selenium import webdriver
# 셀레니움(selenium)을 웹드라이버(webdriver)로부터(from) 불러(import)온다.

from selenium.webdriver.chrome.options import Options
# 셀레니움에 다양한 옵션을 적용시키기 위한 패키지를 불러온다.

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# 크롬드라이버 매니저를 실행시키기 위해 묶어서 불러와준다
user_agent = "Mozilla/5.0"
# 유저 에이전트를 이렇게 내보낸다

options = Options()
options.add_experimental_option('detach', True)
# option 설정을 넣기 위한 초기화 과정
# options에 experimental_option에 detach를 작동 시키는데, 이는 창을 계속 열려있도록 해준다

# options.add_argument("--start-maximized")
# # 화면을 최대 크기로 켜준다. 이외에 여러 옵션들이 있다.
# options.add_argument("--mute--audio")
# # 음소거 모드로 열린다
# options.add_argument('incognito')
# # 시크릿모드
# options.add_argument("--headLess")
# # 창을 띄우는데 화면을 띄우지 않고 작동시킨다. 종료 시킬경우에는 control(command) + C 로 종료

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 크롬이 자동화된 메시지에 의해 제어되고 있습니다. 메시지 삭제하여 차단 당할 확률 감소
# 터미널에 뜨는 메시지를 제거

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# 서비스가 크롬드라이버 매니저를 설치하여 최신 버전으로 유지하게 해준다
# 서비스와 옵션값들을 다 담아준다.


url = "https://kream.co.kr/"
driver.get(url)
# 크림 사이트의 주소를 드라이버에 겟한다.

# 이 전체가 가장 기본적인 옵션으로 쓴다.