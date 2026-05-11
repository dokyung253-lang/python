
# 웹 크롤링: 웹페이지 존재하는 데이터들을 수집하는 기술
# 기초지식 : HTML/CSS(식별자) 필요
# * 파이썬 크롤링 라이브러리 : 정적 - request(내장), BeautifulSoup  / 동적(JS/대기) - Selenium(Java) , Playwright 
# 크롤링(로봇) 허용 여부 확인 : 도메인/robots.txt
#   예] https://www.jobkorea.co.kr/robots.txt , Disallow 불가능, Allow 가능
# 적절한 크롤링으로 윤리적으로 사용하기

# [1] HTML/CSS 식별자(마크업, #id , .class , 자손선택자 띄어쓰기, 자식선택자 >) 찾기
# 프라우저 개발자도구[F12] -> 왼쪽상단에 마우스아이콘( ctrl+shift+c ) 클릭 -> 크롤링 요소 선택 -> 확인

# [2] 파이썬 크롤링
# 네이버 검색어 -> 안양날씨 -> 현재날씨 크롤링
# 1. 주소         : https://search.naver.com/search.naver?query=%EC%95%88%EC%96%91+%EB%82%A0%EC%94%A8
#   - 쿼리스트링(주소상 변수) : URL?변수명=값&변수명=값, 필요한 변수만 정리
#   - url에서는 한글 불가능, 인코딩 필요하다 
# 2. 크롤링 선택자 :.temperature_text

# requests.get( url )

import requests                 # URL 요청 라이브러리
from bs4 import BeautifulSoup   # 요청된 URL의 HTML 조작 라이브러리
response = requests.get("https://search.daum.net/search?w=tot&q=%EC%95%88%EC%96%91+%EB%82%A0%EC%94%A8&DA=UMZ")
print( response )       # <Response [200]>

# [2] 요청(200)된 url에서 HTML형식으로 파싱하기, BeautifulSoup( response.text, "html.parser")
soup = BeautifulSoup( response.text, "html.parser" )
print( soup ) # 마지막에 </html> 확인

# [3] 가져온 HTML에서 특정한 요소(식별자)만 가져오기 ,soup.select_one(식별자)
txt_temp = soup.select_one('.txt_temp')
print( txt_temp )

# [4] 가져온 요소에서 텍스트만 추출, <마크업> *텍스트* </마크업>, 요소변수.get_text()
print( txt_temp.get_text() )  # 18.2
