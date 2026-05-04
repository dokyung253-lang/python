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
result = pd.concat( [ df_info, df_score, ], axis = 0, ignore_index = True )
print( result ) # 세로 연결

result = pd.concat( [df_info, df_score], axis = 1 )
print( result ) # 가로 연결

