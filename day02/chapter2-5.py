# 비교연산자 == != > < >= <=
# 문자열 비교 : 가나다/abc 순으로 앞에 있는 것이 작은 값
print( "가방" == "가방" )
print( "가방" != "하마" )
print( "가방" > "하마" ) # False # 유니코드 '가' vs 유니코드 '하' 코드표 상 앞의 값이 작은 수 

# 범위논리
x = 25
print( 20 <  x < 30 )
print( 40 < x < 60 )

# 논리 연산자 : and or not
print( not True ) # False
print( True and True ) # True
print( True and False ) # False
print( True or False ) # True
