import pandas as pd
# 문제 1: 인덱스 불일치와 결측치 처리
sales = {'mon': 100, 'tue': 200, 'wed': 300}
x = pd.Series(sales)
x = x.rename({ 'mon': '월',  'tue': '화', 'wed' : '수'} )
print('문제1\n',x)

# 문제 2: 슬라이싱을 이용한 부분 수정
data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print( '문제2', data.iloc[1:4] )
z = data[1:4] * 2
data.loc['d'] = 100
print( '문제2\n', data )

# 문제 3: Series 연결과 중복 인덱스 조회
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([3, 4], index=['a', 'c'])
s3 = pd.concat([s1 , s2])
print('문제3\n', s3.loc['a'])

# 문제 4: 복합 조건을 활용한 데이터 변경
data = pd.Series([15, 25, 35, 45, 55])
x = data[ (30<data) & (data<50) ]
print("문제4\n" , x+5 )

# 문제 5: 범주형 데이터의 빈도수 및 비율 분석
grade = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B'])
print('문제5',grade.value_counts() )
print('문제5',grade.value_counts( normalize=True ))

# 문제 6: 산술 연산에서의 인덱스 정렬(Alignment)
s1 = pd.Series([10, 20], index=['a', 'b'])
s2 = pd.Series([30, 40], index=['b', 'c'])
s3 = pd.Series(s1 + s2)
print('문제6', s3)
# a,c에서 발생 , 겹치는 인덱스(짝)가 없어서?


# 문제 7: 다중 정렬 구현 (Values & Index)
data = pd.Series([20, 10, 20, 30], index=['d', 'c', 'a', 'b'])
# 1차 정렬 이후에 유지하기 위해서, 1차정렬에 kind속성에 'stable' 적용하여 유지할 수 있다.
# sort(2차정렬).sort(1차정렬)
result3 = data.sort_index( ).sort_values( ascending=False, kind='stable')
print('문제7', result3)

# 정렬 따로 하는 경우에는 1차 정렬과 2차 정렬 유지 불가능
# x = data.sort_index(ascending= False)     # 1차 정렬 , 값 내림차순
# data = data.sort_index()                  # 2차 정렬 , 인덱스 오름차순
# print( data ) 

# 문제 8: 그룹화 및 다중 집계 함수 적용
data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'A', 'B'])
x = data.groupby(level=0).sum
x = data.groupby(level=0).mean()
x = data.groupby(level=0).agg(['sum','mean'])
print('문제8', x)

# 문제 9: 가중 평균(Weighted Average) 계산
# 각 과목의 가중 점수weight를 합산한 최종 총점을 브로드캐스팅 연산을 통해 구하시오.
score = pd.Series([80, 90, 70], index=['math', 'eng', 'sci'])           # 점수
weight = pd.Series([0.4, 0.3, 0.3], index=['math', 'eng', 'sci'])       # 가중점수
x = (score*weight).sum()        # 각 과목의 가중 점수를 합산한 최종 총점을 브로드캐스팅 연산을 통해 구하시오
print('문제9', x)


# 문제 10: 필터링 및 인덱스 재설정 (Reset Index)
# 2. 추출된 Series의 기존 문자 인덱스를 제거하고 0부터 시작하는 숫자 인덱스로 재설정하시오.
data = pd.Series([10, 30, 20, 40], index=['a', 'b', 'c', 'd'])
x = data[data>25]
x = x.reset_index(drop=True)    # 2. 추출된 Series의 기존 문자 인덱스를 제거하고 0부터 시작하는 숫자 인덱스로 재설정하기
print("문제10", x)


