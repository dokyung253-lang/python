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

# 확인문제 p.266
print("{:b}".format(10)) # 1010
print( int("1010", 2))   # 10

print("{:o}".format(10)) # 12
print( int("12", 8))     # 10

print("{:x}".format(10)) # a
print(int("10", 16))     # 16

print("안녕안녕하세요".count("안")) # 2

# 확인문제 2
output = [ i for i in range(1, 101) 
          if "{:b}".format(i).count("0") == 1]

for i in output :
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))


# 확인문제 p.290
def f(x):
    return x
print(f(10))

def f(x):
    return 2 * x + 1
print(f(10))

def f(x):
    return (x+1)**2
print(f(10))

def mul(*values):           # 가변 매개변수는 리스트 타입이다. 
    result = 1;             # 모두 곱한 결과를 저장하는 변수
    for value in values :   # 리스트 반복문
        result *= value     # 하나씩 곱한다.
    return result           # 함수 종료 시 모두 곱한 결과 리턴/반환

print(mul(5,7,9,10))

# 확인문제1 (p.315)
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람수 = 6 
memo = {}

def 문제( 남은사람수, 최소사람수 ):         # 100, 2
    key= str( [남은사람수, 최소사람수])
    if key in memo :
        return memo[key]
    if 남은사람수 < 0 :
        return 0
    if 남은사람수 == 0 :
        return 1
    
    count = 0                           # 인원수
    for i in range( 최소사람수, 앉힐수있는최대사람수 + 1 ) : # 2(최소사람수)부터 11(앉힐수있는최대사람수+1)까지 1씩 증가 반복
        count += 문제( 남은사람수 -i, i)                   # 남은사람수에 i만큼 제외하고 , i대입

    return count
print( 문제( 전체사람수, 앉힐수있는최소사람수 )) 