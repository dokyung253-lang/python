# 확인문제 p.247
#1 
a = range(5)
print( list(a) )
a = range( 4, 6 )
print (list(a))
a = range( 7, 0, -1)
print( list(a))
a = range(3, 8)
print(list(a))
a = range(3, 10, 3)
print(list(a))

# 2
key_list = ['name', 'hp', 'mp', 'level']
value_list = ['기사', 200, 30, 5]
character = {}

#0부터 마지막 인덱스까지
for 반복변수 in range( 0, len(key_list) ):
    key = key_list[반복변수]
    print(key)
    value = value_list[반복변수]
    print( value )
    character[key] = value

print(character)

# 3
limit = 10000
i = 1
sum_value = 0;
while True :            # 파이썬에는 true 대신에 True 사용
    sum_value += i      # 누적합계
    if sum_value > limit :  # # 만약에 누적합계가 10000보다 커지면
        break           # 가장 가까운 반복문 탈출
    i += 1              # 1씩 증가
print( i, sum_value )

# 4
max_value = 0
a = 0
b = 0

for i in range( 1, 51 ) : 
    j = 100 - i
    if max_value < i * j:
        max_value = i * j
        a = j
        b = i

print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))