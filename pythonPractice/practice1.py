#문제 1: 원의 넓이 계산 반지름을 input()으로 입력받아 원의 넓이를 계산하여 출력하시오. (원주율은 3.14로 계산)
radios = float(input("반지름을 입력하세요 > "))
area = (radios**2)*3.14
print(area)

#문제 2: 평균 점수 계산기 국어, 영어, 수학 세 과목의 점수를 각각 입력받아 총점과 평균을 구하여 출력하시오.
int_a = int(input("국어점수: "))
int_b = int(input("영어점수: "))
int_c = int(input("수학점수: "))
total = int(int_a + int_b + int_c)
print( total )
average = int (total / 3)
print (average)

#문제 3: 나머지 연산 활용 정수 하나를 입력받아 그 수가 짝수이면 0, 홀수이면 1이 출력되도록 작성하시오.
a = int(input("숫자: "))
result = a % 2
print(result)

#문제 4: 거듭제곱 계산 숫자 하나를 입력받아 해당 숫자의 제곱과 세제곱 값을 각각 출력하시오.
int_a = int(input("정수를 입력하세요 : "))
int_b = int_a**2
print(int_b)
int_c = int_a**3
print(int_c)

#문제 5: 복합 대입 연산자 실습 변수 balance에 5000을 저장한 후, 복합 대입 연산자만을 사용하여 2000을 더하고, 다시 1500을 뺀 최종 값을 출력하시오.
balance = 5000
balance += 2000
balance -= 1500
print(balance)

#문제 6: 문자열 길이 출력 사용자의 영문 이름을 입력받아 "당신의 이름은 [숫자]글자입니다."라고 출력하시오.
name = str(input("영문 이름 : "))
name2 =len(name)
print("당신의 이름은 [", str(name2), "]글자 입니다. ")

#문제 7: 성과 이름 분리 "홍 길동"과 같이 공백이 포함된 이름을 입력받아, 인덱싱과 슬라이싱을 사용하여 성(첫 글자)만 출력하시오.
full_name = input("공백을 포함한 이름을 입력하세요 (예: 홍 길동): ")
print(full_name[0])

#문제 8: 문자열 "Python"이 저장된 변수에서 콜론 하나(:)를 사용하는 슬라이싱을 통해 "Pyth"까지만 추출하여 출력하시오.
str_1 = "Python"
print(str_1[:4])

#문제 10: 문자열 곱셈 연산 사용자로부터 문자열 하나와 숫자 하나를 입력받아, 해당 문자열을 숫자만큼 반복하여 출력하시오.
str_a = str(input("문자 : "))
int_a = int(input("숫자 : "))
print(str_a * int_a)

#문제 11: 정수형 변환 실수 3.9를 변수에 저장하고, 이를 정수형으로 변환하여 출력했을 때 소수점이 사라지는 것을 확인하시오.
a =  3.9
print( int(a) )

#문제 12: 두 수의 문자열 결합 두 개의 숫자를 입력받되, 계산이 아닌 문자열로 결합하여 출력하시오. (예: 10과 20 입력 시 1020 출력)
int_a = str(input("숫자1 : "))
int_b = str(input("숫자2 : "))
print(int_a + int_b)

#문제 13: 자동 형변환 확인 정수 10을 실수 2.0으로 나눈 결과를 출력하고, 해당 결과의 데이터 타입이 무엇인지 출력하시오.
a = int(10)
b = float(2)
c = a/b
print(c)
print(type(c))

#문제 14: 초를 분/초로 환산 전체 초(second)를 입력받아 몇 분 몇 초인지 계산하여 출력하시오. (예: 70초 -> 1분 10초)
total_sec = int(input("전체 초: "))
min = int(total_sec // 60)
sec = int(total_sec % 60)
print( str(min)+"분 "+ str(sec)+"초" )
