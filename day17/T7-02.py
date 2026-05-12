import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# (1) 크롤링 주소 : https://www.yes24.com/product/category/daybestseller?categoryNumber=001
# url = 'https://www.yes24.com/product/category/daybestseller?categoryNumber=001'

book_list=[]
# (2) 주소 매개변수 분석, categoryNumber=001&pageNumber=1&pageSize=24&type=day&saleDts=&sex=F
# 1~3페이지 크롤링 예
for page in range( 1, 4 ) : #range( 시작, 끝 전까지 ) # 1~3
    url = f'https://www.yes24.com/product/category/daybestseller?pageNumber={page}'
    # f'문자열{변수/계산식}문자열{변수/계산식}'

    # (3) url 요청
    response = requests.get( url )

    # (4) 요청한 url의 성공했을 때 html로 파싱
    soup = BeautifulSoup( response.text, 'html.parser' )
    # (5) 가져올 식별자, .soup.select() : 여러개 선택, .soup.select_one() 하나 선택
    books = soup.select( '#yesBestList > li')
    # 책 여러개 : #yesBestList 여러개책정보, li(책 하나) 
    # 책 하나당 (.gd_name 책 제목, .yes_b 책 가격, .info_auth 저자정보)
    for book in books : # <li> 여러개이므로 반복문 가능
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        info_auth = book.select_one('.info_auth').get_text().strip().replace('\n', '')
        # (6) 리스트에 딕셔너리 포함하기
        book_list.append( {"제목": gd_name, "가격": yes_b, "저자정보" : 'info_auth'} )
    # (7) import time, time.sleep(초) , 지정한 초 만큼 코드(스레드) 대기, 여러개 크롤링 시 과부하 방지 
    time.sleep(2)

# (8) 판다스에 넣어주기
print( book_list )    
df = pd.DataFrame( book_list )
print( df )