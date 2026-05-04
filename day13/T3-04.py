# 파이썬 : 데이터 시각화
# 맷플롯립 : 원초적인 차트(기본)
# 씨본 : 맷플롯립보다 세부적인 기능 지원(상관관계 o, 통계나 예측 결과 예상 시에 자주 사용됨 ) 

# [1] 맷플로립 설치 : pip install matplotlib
import matplotlib as mpl
# print( mpl.__version__) # 3.10.9

# 관례적 import하는 방법
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# 시각화란? 데이터 분석 결과를 시각적으로 표현하여 인사이트(특징) 도출

# [*] 차트 내  한글 깨짐 방지 폰트 
import matplotlib as mpl
mpl.rc('font', family='Malgun Gothic')      # 한글 폰트 설정( 윈도우 기준 설치된 폰트 )
mpl.rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지

# 1. 선 그래프1 , '추세'를 구할 때 사용
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # x축(가로축의 값)
y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # y축
# 2. 그래프 설정
# plt.plot( x, y )              # .plot( x값, y값 )
# plt.title('Line Chart Exam')  # .title('차트제목')
# plt.xlabel( 'X-axis Title' )  # .xlabel('x축 제목') 
# plt.ylabel( 'Y축 제목' )  # .ylabel('y축 제목')
# plt.grid(True)                # .grid(True), 눈금선 표시
# 그래프 출력
# plt.show()  

# [2] 선 그래프2
y2 = [0,1,2,3,4,5,6,7,8,9]
# plt.plot(x, y , label = '감소하는 선(항목명)', color = 'blue', linestyle = ':' )
# plt.plot(x, y2, label = '증가하는 선(항목명)', color = '#FF0000', linestyle = '-' )
# plt.legend()    # 범례에 항목명 표시  # 범례 = legend = 그래프가 무엇을 나타내는 지 좌/우측에 색깔 + 그래프명 적어놓은 것
# plt.show()

# [3] 막대 그래프 , 데이터의 '비교',  .bar( x축값, y축값, width = 굵기, label = '항목명' ,color = '색상')
categories = ['학생1', '학생2', '학생3', '학생4']
values     = [    85,    92  ,     78, 85     ]   
values2    = [    85,    87  ,     95, 85     ]

# 막대 겹치지 않게 표시 , width='막대굵기' , *인덱스(위치번호) 사용한 크기 조정*
import numpy as np
x = np.arange( len(categories) ) # 0부터 x축의 값 개수 만큼 생성 0~3
# plt.bar( x - 0.2 , values , width = 0.4, label = '국어성적', color = 'blue')  # 선차트 : plot   # 막대차트 : bar
# plt.bar( x + 0.2, values2, width = 0.4, label = '수학성적' ,color = 'orange')
# plt.title('학생 성적 비교')
# plt.xlabel('학생명')
# plt.ylabel('성적점수')
# plt.legend()
# plt.grid( axis ='y')  # 눈금선(y축만)
# plt.xticks( x, categories ) # 위치(0~3) 순으로 라벨(학생1 ~ 학생4) 지정
# plt.show()


# [4] 파이그래프, 백분율, .pie( 값, labels = '항목명', colors = '색상', explode = '강조', startangle = 시작 기울기(각도), autopct='비율표시' )
labels = ['피자', '햄버거', '샐러드', '파스타']
sizes  = [40, 30, 20, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = [ 0.1 , 0, 0, 0]   # 전체 그래프에서 조각이 튀어나오는 정도(강조)
plt.pie( sizes, labels = labels, colors = colors, explode = explode, startangle= 90 , autopct= '%1.1f%%' )  
# %형식문자 %자릿수.소수자릿수f, f: 실수, %% : 기호'%' 표시
# plt.title('음식 선호도')
# plt.show()

# [5] 선점도 , 밀집도 , .scatter( x축값, y축값 , c(color) = , s(size) = 점크기)
x = [1.5 , 2.5, 3.5, 4.5, 5.5]
y = [50, 60, 65, 70, 75]
# plt.scatter(x,y, c = 'red', s = 25)
# plt.grid()
# plt.show()

# [6] 히스토그램, 상관관계 , .hist( 값, color='' , alpha = 투명도, bins = 구간 갯수 )
# 샘플데이터
data = []
for i in range( 500 ) : # 50번 반복
    value = sum( [ (i * j) % 100 / 100 for j in range(1, 13) ] )      # 리스트 내포 ( 1차원 리스트 생성)
    # (i * j) % 100 : 나머지값 계산
    # /100 : 0~1사이 값으로 계산
    # sum() : 총합계 , 즉] 13개의 0~1 사이의 난수를 만들어서 총 합계 (중앙값이 큰 난수 생성 예정)
    data.append( value )
# 차트 만들기
# plt.hist( data , color = 'skyblue' , alpha = 0.7 , bins = 60 )
# plt.show()

# [7] 다중그래프 표현, .subplot( 행개수, 열개수, figsize = (가로, 세로) ) 
fig , axs = plt.subplots(1, 2 , figsize = (20, 7)) # 한줄에 2개의 차트
# fig : 다중그래프를 가지고 있는 전체 그래프
# axs : 다중그래프의 위치 , axs[0] 첫번째 그래프, axs[1] 두번째 그래프
# figsize : ( 가로, 세로 ) , 전체 그래프의 가로 inch

axs[0].plot( [1,2,3] , [1,4,9] )
axs[0].set_title('선그래프')        # 주의할 점 : .title() 전체 그래프의 제목, .set_title() : 하위 그래프의 제목
axs[0].set_xlabel('x축제목')        # 즉] 하위 .title. , .xlabel, .ylabel등에서는 set_XXXX()으로 사용하기
axs[0].set_ylabel('y축제목')
axs[1].bar( [1,2,3], [3,5,2] )
axs[1].set_title('막대그래프')
axs[1].set_xlabel('x축제목')
axs[1].set_ylabel('y축제목')
plt.savefig('./day13/save_chart.png')
# plt.savefig('저장경로') # 그래프 이미지 다운로드

plt.show()

# fig, axs = plt.subplots( 2, 2 ) # 행 = 2, 열 = 2, 총 그래프 수 = 4
# axs[0][0].plot()
# axs[0][1].bar()
# axs[1][0].scatter()
# axs[1][1].pie()

