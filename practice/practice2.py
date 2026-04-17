# [ Python practice2 ]
# [ 단 ] for(반복문)은 사용하지 않습니다.
# [ 제출방법 ] 코드가 작성된 파일이 위치한 깃허브 상세 주소를 제출하시오.


# 문제 1: 대소문자 변환
# 사용자로부터 영문 문장을 입력받아 전체를 대문자로 변환한 결과와 소문자로 변환한 결과를 각각 출력하시오.
a = input("영문 입력:")
print(a.upper())
print(a.lower())


# 문제 2: 공백 제거 및 문자 교체  * 문제있음
# 사용자로부터 " Python Programming "과 같이 공백이 포함된 문자열을 입력받아 양쪽 공백을 제거하고, 공백 부분을 언더바(_)로 교체하여 출력하시오.
b = input("문자열 입력: ")
result = b.strip()
result = b.replace(" ", "_")
print(result)


# 문제 3: 문자열 찾기 (인덱스)  * 문제 있음
# 문자열 "Hello, Python World!"에서 "Python"이라는 단어가 시작되는 위치(인덱스)를 찾아 출력하시오.
str_pyt = "Hello, Python World!"
c = "Python"
if c in str_pyt : 
    print(str_pyt.find('Python'))


# 문제 4: 두 점수의 합격 판별
# 두 개의 점수를 입력받아 총점이 120점 이상이고 각 점수가 모두 50점 이상이면 "합격", 아니면 "불합격"을 출력하시오.
input_a = int(input("첫번째 점수: "))
input_b = int(input("두번째 점수: "))
if input_a + input_b >= 120 and input_a >= 50 and input_b >= 50 :
    print("합격")
else :
    print("불합격") 


# 문제 5: 아이디 및 비밀번호 검증
# 저장된 db_id = "user01", db_pw = "pass12"와 사용자가 입력한 정보가 모두 일치하면 "성공", 하나라도 다르면 "실패"를 출력하시오.
db_id = "user01"
db_pw = "pass12"
id_input = input("아이디 : ")
pwd_input = input("비밀번호 : ")
if id_input == "user01" and pwd_input == "pass12" :
    print("성공")
else :
    print("실패") 

# 문제 6: 비밀번호 보안 등급
# 비밀번호를 입력받아 길이가 10자 이상이면 "강함", 5자 이상 10자 미만이면 "보통", 5자 미만이면 "약함"을 출력하시오.
pwd = input("비밀번호: ")
if len(pwd) >= 10 :
    print("강함")
elif 10 > len(pwd) > 5 :
    print("보통")
else :
    print("약함")


# 문제 7: 성별 판별 *문제 있음
# 주민등록번호 뒷자리 첫 번째 숫자를 입력받아 1 또는 3이면 "남자", 2 또는 4이면 "여자"를 출력하시오. (힌트: in 연산자 활용)
id_num = input("주민등록 뒷자리숫자: ")
if id_num[0] in ["1", "3"] :
    print("남자")
elif id_num[0] in ["2", "4"] :
    print("여자")
else :
    print(None)


# 문제 8: 입장료 계산
# 나이를 입력받아 65세 이상이거나 7세 이하이면 "무료", 그 외에는 "10,000원"을 출력하시오.
age = int(input("나이: "))
if age >= 65 or age <= 7 :
    print("무료")
else :
    print("10,000원")


# 문제 9: 문자열 포함 여부
# 사용자가 입력한 문장에 "금지어"라는 단어가 포함되어 있으면 "차단된 문장입니다", 없으면 "정상 문장입니다"를 출력하시오.
input_c = str(input("문장을 입력하세요: "))
if "금지어" in input_c :
    print("차단된 문장입니다.")
elif "금지어" not in input_c :
    print("정상 문장입니다.")


# 문제 10: 성적 등급 산출
# 점수를 입력받아 90점 이상은 "A", 80점 이상은 "B", 70점 이상은 "C", 그 미만은 "F"를 출력하시오.
score = int(input("점수 : "))
if score >= 90 :
    print("A")
elif score >= 80 : # elif는 앞의 조건이 false일 때만 출력됨 -> 따라서 조건문에도 90> score을 쓸 필요없음
    print("B")
else :
    print("F")

# 문제 11: 할인 적용 결제 금액
# 구매 금액을 입력받아 10만원 이상이면 20% 할인, 5만원 이상이면 10% 할인, 그 미만은 할인이 없는 최종 결제 금액을 출력하시오.
purchase_amount = int(input("구매 금액 : "))
if purchase_amount >= 100000 :
    print("최종금액 :", purchase_amount - (purchase_amount*0.8))
else :
    print("최종금액 :" , purchase_amount )


# 문제 12: 가위바위보 결과
# 플레이어1과 플레이어2가 각각 낸 가위(0), 바위(1), 보(2) 숫자를 입력받아 플레이어1 기준으로 "승리", "패배", "무승부" 중 하나를 출력하시오.
print("<가위(0)바위(1)보(2) Game>")
p1 = int(input("Player1 : "))
p2 = int(input("Player2 : "))
if (p1 == 0 and p2 == 2) or ( p1 == 2 and p2 == 1) or (p1 == 1 and p2 == 0) :
    print('승리') 
elif (p1 == 0 and p2 == 1) or (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 0) :
    print('실패')
elif ( p1 == p2 ) :
    print('무승부')
else :
    print("")


# 문제 13: 닉네임 설정
# 닉네임을 입력받아 이름이 "관리자"와 일치하면 "[관리자]님 환영합니다", 아니면 "[닉네임]님 안녕하세요"를 출력하시오. (힌트: .format() 활용)
nick_n = str(input("닉네임 : "))
if nick_n == "관리자" :
    print("[{}]님 안녕하세요".format(nick_n))
else :
    print("[{}]님 안녕하세요".format(nick_n))
