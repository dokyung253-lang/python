import numpy as np
# 문제 1: 배열의 병합 (Concatenate)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print( np.concatenate((x,y), axis = 0))
print( np.concatenate((x,y), axis = 1))

# 문제 2: 배열 정렬 (Sorting)
x = np.array([3, 1, 2, 5, 4])
print( np.sort(x) )
print( np.sort(x)[::-1] )

a = np.array([[3, 1, 2], [9, 8, 7]])
print( np.sort( a, axis = 0 ) )
print( np.sort( a, axis = 1 ) )

# 문제 3: 다중 조건 정렬 (lexsort)
x = np.array([25, 30, 22, 24])
y = np.array(["철수", "영희", "민수", "영희"])
z = np.lexsort((x,y))
print("3번", z )
print( y[z], x[z] )


# 문제 4: 조건 검색과 필터링 (Boolean Indexing).
x = np.array([10, 20, 30, 40, 50])
print(x[x > 30])                # [ ] 안은 원래 인덱스 자리, 조건 필터링도 가능
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x[x>5])

# 문제 5: np.where를 이용한 조건 처리
x = np.array([10, 20, 30, 40, 50])
y = np.where(x > 25 , x, -1)
print(y)
print( np.extract(x<30, x))

# 문제 6: 마스크 배열(Masked Array)
x = np.array([1, 2, 3, 4, 5])
con1 = x % 2 == 1
print( np.ma.array( x, mask = con1 )  )
print( np.ma.sum(con1))


# 문제 7: 비트 연산자를 이용한 복합 조건 검색
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([15, 22, 35, 45, 55, 65, 75, 85])
print( x[ (x > 30) & (y < 50)] ) 
print( x[ ~(y < 50) ] )

# 문제 8: 기본 통계 함수 (Min, Max, Sum, PTP)
x = np.array([1, 2, 3, 4, 5])
print( np.min(x))
print( np.max(x))
print( np.sum(x))
print( np.ptp(x))

# 문제 9: 평균, 중앙값, 분산, 표준편차
# 1. 전체 요소의 평균(mean)과 중앙값(median)을 구하시오.

# 2. axis=0(열 방향) 기준의 표준편차(std)와 axis=1(행 방향) 기준의 분산(var)을 구하시오.
x = np.array([[1, 2, 3], [4, 5, 9]])
print( np.mean(x))
print( np.median(x))
print( np.std(x, axis= 0) , np.var( x, axis=0 ) )

# 문제 10: 사분위수와 IQR 계산

# 배열 x = np.array([10, 20, 30, 40, 50])에 대하여 다음 통계량을 구하시오.

# 1. 1사분위수(25%)와 3사분위수(75%)

# 2. 3사분위수에서 1사분위수를 뺀 사분위수 범위(IQR) 값

x = np.array([10, 20, 30, 40, 50])
print( np.percentile(x,25), np.percentile(x,75) )
print( np.percentile(x,75) - np.percentile(x,25) )