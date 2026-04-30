# customer_purchase_data.csv 다운로드 받아서 현재 py 파일과 같은 폴더에 저장
import numpy as np

# 1. .csv ( ,쉼표로 구분한 자료의 형식 )파일 가져오기
# data = np.genfrom.txt("파일경로", delimiter='구분문자', skip_header=제외할헤더(행)수)
data = np.genfromtxt(
    "./numpyPractice/customer_purchase_data.csv",
    delimiter=',', 
    skip_header=1)

# 가져온 데이터의 넘파이 형식 확인하기
print( data.shape )

# 1 특정 열, 행 추출 | 평균
sales = data[:, -1]
print( sales )
print('평균: ', np.mean(sales),'총매출액: ', np.sum(sales))

# 2 조건 필터링
x = data[:, 1] >= 20
y = data[:, -1] >= 2000
result = data[x&y]
print( result[:,0] )

# 3 통계 , max()
arpy = data[:, 4] / data[: , 1]
print( np.max(arpy) )       # 최댓값 525.0 
print( x/y )                # [0.3 0.3 0.3] 주의할 점 : 배열 연산 시 동일한 위치끼리 연산

findIndex = np.argmax(arpy)     # 최댓값의 인덱스 위치
print( data [findIndex , 0])

# 4 전체에서 몇 명인지 <----> 조건 True 개수
cont1 = (data[:, 1] <= 3) & (data[:, 3] <= 1)    # 조건에 따른 True만 추출
print( np.sum( cont1 ) )

# 5 정규화, 공식 : (값(가격) - 최솟값) / (최댓값 - 최솟값) 
# 어떠한 자료들을 0과 1 사잇값으로 만들어서 백분율화(0:0% ~ 1:100%), 비교 용이
# 0.9 : 90% , 상위 10% 위치한 구매가격 가진 고객들
data_min = np.min(data[:, 4])
print(data_min)
data_max = np.max(data[:, 4])
print( data_max )
norm_data =  (sales- data_min) / (data_max - data_min) 
vip_data = norm_data >= 0.9
print( vip_data )
print( data[vip_data] )
#--------------------------------------
x = np.array([True, False, True])
y = np.array([1, 2, 3])
print(y[x])     # [1 3]