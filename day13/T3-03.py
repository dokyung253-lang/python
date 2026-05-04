import pandas as pd

# [13] 판다스 병합( SQL JOIN ) , .merge( x, y , on = '공통컬럼명(pk/fk)', how='inner/outer/left/right' )
df_info = pd.DataFrame( {'ID' : [1,2,3], 'Name' : ['Ant', 'Bee', 'Cat'] } )
df_score = pd.DataFrame( { 'ID' : [2,3,4], 'Score' : [88,92,85] } )

# 두 판다스 간의 ID가 같은(교집합) 자료 병합
result = pd.merge( df_info, df_score, on = 'ID', how = 'inner' ) # 공통된 컬럼명(2,3)을 병합
print( result )

result = pd.merge( df_info, df_score, on = 'ID' , how = 'right' ) # left : 왼쪽 전체 + 교집합 / right : 오른쪽 전체 + 교집합 / outer : 여집합
print( result )

# [14] 판다스 합치기, .concat( [x, y] , axis = 0(행)/1 )
result = pd.concat( [ df_info, df_score, ], axis = 0, ignore_index = True )  # 기존 인덱스를 무시하고 새롭게 0부터 번호를 매기는 방식
print( result ) # 세로 연결

result = pd.concat( [df_info, df_score], axis = 1 )
print( result ) # 가로 연결

new_score = pd.Series( [85, 90, 88], name = 'Score' )       # 새로운 열(시리즈)
df_info['NewScore'] = new_score  # 새로운 열(시리즈)
print( df_info )

# [15] 정렬, 
# .sort_values( by='정렬기준', ascending = True(오름차순)/False(내림) )
# .sort_values( by=['1차정렬', '2차정렬'], ascending=[ 1차정렬 , 2차정렬 ] ) 
# .sort_index( axis = 0(행)/1(열) , ascending=True(오름)/False(내림) )

x = { 
    'Name' : ['Ant', 'Bee', 'Cat', 'Dog'],
    'Age'  : ['27', '27', '22', '32'],
    'Score': [88, 95, 85, 90]  }
df = pd.DataFrame(x)

# 점수기준 내림차순
result = df.sort_values( by='Score', ascending = False ) 
print( result )     

# 나이기준 오름차순 이후, 점수 기준으로 내림차순 ( 즉] 나이정렬 후 동일한 나이끼리 점수 내림차순 )
result = df.sort_values( by=['Age', 'Score'], ascending=[ True , False ] )  
print( result )

# 열이름(라벨) 내림차순으로 정렬
result = df.sort_index( axis = 1, ascending= False )
print( result )

# [16] 그룹, 
# .groupby('그룹기준')['집계기준'].집계함수()
# .groupby( ['1차그룹', '2차그룹'] )['집계기준'].집계함수()

df = pd.DataFrame( {
    'Category' : ['A','A','B','B','A','B'],
    'Type' : ['X','Y','X','X','Y','Y'],
    'Values' : [10, 20, 30, 40, 50, 60]
})

df.groupby('Category')['Values'].sum()  # 카테고리 별 값 합계
print( result )
result = df.groupby('Category')['Values'].mean()  # '타입'별 '값' 평균
print( result )
# 다중 그룹
result = df.groupby( ['Category', 'Type'] )['Values'].sum()
print(result)
# 다중 집계
result = df.groupby( ['Category','Type'] )['Values'].agg( ['sum', 'mean', 'count'])
print( result )
result = df.groupby( ['Category','Type'] )['Values'].describe()
print( result )
