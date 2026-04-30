import pandas as pd
# 판다스
# pd.Series    # 1차원
# pd.DataFrame # 2차원
# 데이터프레임 생성 , pd.DataFrame(2차원리스트/딕셔너리,넘파이배열 , column = [열이름], index=[행이름])
# [1] 데이터프레임 생성 , pd.DataFrame(2차원리스트 , column = [열이름])
data_list = [['콩순','5','seoul'], 
             ['우리','1','kyeongki'],
             ['율무','10','Incheon']]
x = pd.DataFrame( data_list, columns=['name', 'age','city'] )
print(x)

# [2] 데이터프레임 생성2, pd.DataFrame(딕셔너리), 대부분의 공공자료는 *딕셔너리*
data_dict = {'name':['ant','bee','cat'],
             'age':['25','30','21'],
             'city':['seoul','busan','daegu']} # 딕셔너리
x = pd.DataFrame(data_dict)
print(x)

# [3] 데이터프레임 생성3, pd.DataFrame(넘파이배열, columns = [열이름])
import numpy as np
data_np = np.array(data_list)
x = pd.DataFrame(data_np, columns=['name', 'age', 'city'], index=['a','b','c'])
print(x)

# [4] 
print( x.shape )       # (3,3) 행/열 크기
print( x.columns )     # 컬럼(열) 목록
print( x.index )       # 인덱스(행) 목록
print( x.values )      # 값만 2차원으로 반환 
print( x.head(2) )     # 상위 n개만 반환
print( x.tail(2) )     # 하위 n개만 반환
x.info()               # 전처리(데이터정리) 하기 전 결측치 *확인*

# [5] 인덱싱
print( x.iloc[0] )     # iloc[인덱스번호]
print( x.iloc[1,2] )   # iloc[행, 열]
print( x.loc['a'] )    # loc[라벨명]
print( x.loc['b', 'city'] ) # loc[라벨명, 컬럼명]

# [6] 슬라이싱 , [ 시작 인덱스 : 끝 인덱스 ] , [ 시작라벨명 : 끝 라벨명 ]
print( x.iloc[0:2, 0:1])                # [ 행슬라이싱, 열슬라이싱 ]
print( x.loc['a':'b', 'name':'city'])   # [ 행슬라이싱, 열슬라이싱 ]

# [7] 새로운 열 추가 , ['새로운열'] = 새로운값 , .assign(새로운열 - 새로운값)
x['score'] = [100, 80, 95]          # 파괴적(원본 수정)
print(x)

x = x.assign(score2 = [87, 65, 78]) # 비파괴적( 새로운 판다스 반환)
print(x)

# [8] 특정한 값 수정 , [기존열] = 수정할값
x['age'] = [31, 52, 40]
print(x)

x.loc['b', 'age'] = 70          # b행의 age열 값을 70으로 변경/수정
print(x)

x.iloc[0,0] = 'apple'           # 0행의 0열 값을 'apple'으로 변경/수정
print(x)

# 여러개 한 번에 수정,
# loc[ [시작라벨 : 끝라벨], 수정할컬럼라벨] ] = [새로운값]
# iloc[[시작인덱스 : 끝인덱스], 수정칼럼인덱스] = [새로운값]
x.loc[['a','b'], 'score'] = [10, 20]
print(x)

# [9] 필터링, x[조건식], x[x[열이름]> y]
cont1 =  x['score2'] > 70 
print( cont1 )                # True, False, True
print( x[ cont1 ] )           # 데이터프레임[조건]

cont2 = x['age'] > 35       # 2번쨰 조건
print( x[ cont1& cont2 ] )    # 1번째 조건과 2번째 조건으로 논리연산
print( x[ cont1 | cont2 ] )


# [10] 필터링 조건으로 새로운 열 추가 또는 수정
x.loc[ x['score2'] > 70 , 'passed'] = True
x.loc[ x['score2'] <= 70 , 'passed'] = False
print(x)


# [11] 열(컬럼) 이름 수정 , .rename( index={ }, columns={'old':'new'})
x = x.rename( columns={ 'city' : '도시' , 'age' : '나이'} )
print(x)

# [12] 집계 , .describe(): 수치자료들을 집계 요약 , x[열이름].집계함수()``
print( x.describe() )
print( x['나이'].sum() )     
print( x['score'].mean())
print( x['passed'].value_counts() ) # 특정 열의 빈도 확인