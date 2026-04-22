# 예외처리 : 예외 발생 시, 프로그램이 강제 종료되지 않게 흐름 제어하는 것 
# 쓰는 이유 : 예외가 발생할 상황을 예측하고 모두 조건문으로 처리하는 것은 매우 힘듦. 
# try : !~ except : ~

try :
    # 예외가 발생할 것 같은 코드
    number_input_a = int( input('정수입력 : '))     # 7: 정상, a: 예외발생

except :
    # 만약에 예외가 발생했을 때 코드
    print('정수만 입력하세요.')

# pass : 예외처리 대신 배제하고 넘어감
list_input_a = ["52", "273", "32", "spy", "103"]
list_number = []
for item in list_input_a :
    try :
        float( item )               # float( ) 실수타입으로 변환 함수
        list_number.append( item )
    except :
        pass                        # 예외 발생 시, 아무것도 실행 안하고 통과
print( list_number )

# else : 예외가 발생하지 않았을 때 실행 코드
try :
    number_input_a = int( input('정수입력 : '))
except :
    print('정수를 입력하세요.')
else : 
    print( number_input_a )

# finally : 무조건 실행할 코드
try:
    number_input_a = int(input("정수 입력 :"))
except:
    print("정수를 입력하세요.")
else:
    print("예외가 발생하지 않았다.")
finally:
    print('무조건 실행되는 코드')



# 확인문제
numbers = [52, 273, 32, 103, 90, 10, 275]
print("- {}는 {}위치에 있습니다.".format(52, numbers.index(52)))
print()

number = 10000
try: 
    if number in numbers:
        print("- {}는 {}위치에 있습니다.".format(number, numbers.index(number)))
except:
    print("- 리스트 내부에 없는 값입니다.")
print()

print("---정상적으로 종료되었습니다.---")

