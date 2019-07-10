'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

string = input('문자를 입력하세요: ')
# 아래에 코드를 작성해 주세요.
print(f"첫글자는 {string[0]}, 마지막 글자는 {string[-1]}입니다")   # -1 인덱스 접근은 가장 마지막이다.

# 0
# apple
#     -1

'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.

# range(1,numbers +1)
for i in range(numbers):
    print(i+1)

'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

# 위의 주석을 풀고 아래에 코드를 작성해 주세요.
if not number % 2:   # not을 이용하면 True,False 값을 바꿀 수 있다.
    print(f"{number}는(은) 홀수입니다.")
else:
    print(f"{number}는(은) 짝수입니다.")

'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

# 위의 4줄의 주석을 풀고 아래에 코드를 작성해 주세요.
# and, or 사용가능

if a >= 90 and b > 80 and c > 85 and d >= 80 :
    print(True)
else:
    print(False)


'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.


    # # 1. 반복문
    # int_price = []
    # for price in prices:
    #     int_price.append(int(price))
    # print(int_price)

    # # 2. list comprehension
    # int_price2 = [int(price) for price in prices]
    # print(int_price2)

    # # 3. map : 첫번째 인자의 함수를 두번째 인자를 반복하며 적용.
    # 반복 가능한 객체에 함수를 각각 적용.
    # int_price3 = list(map(int,prices))
    # print(int_prices3)


a = list(map(int,prices.split(';')))
# b = a.sort()
b = sorted(a, reverse = True)
print(b)
# list.sort() : return이 None. 원본 리스트 자체를 변경
# sorted(list) : return이 정렬된 리스트. 원본 자체는 변경하지 않음.
