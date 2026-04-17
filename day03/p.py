numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number%2==0:
        print( number,"은 짝수입니다")
    else :
        print( number,"은 홀수입니다" )

for number in numbers:
    if len(str(number))>=0:
        print( number,"는", len(str(number)), "자릿수입니다.")
    else :
        print("")

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [ [], [], []]
for number in numbers:
    output = [[number%3-1]].append(number)

print(output)

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(numbers) // 2):
    # j가 1, 3, 5, 7이 나오려면
    # 어떤 식을 사용해야 할까요?
    j = i*2+1
    print(f"i = {i}, j = {i}")
    numbers[j] = numbers[i] **2

print(numbers)