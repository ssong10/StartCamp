import random
import pprint
import requests
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"

# 1. 요청
    # json -> 
    # 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
    # 응답 (HTML, XML, JSON) 3가지 배움
response = requests.get(url).json()
# pprint.pprint(response)
# print(type(response))

first = 0
second = 0
third = 0 
fourth = 0
fifth = 0
bomb = 0


lotto = []
for i in range(1,7):
    lotto.append(response[f'drwtNo{i}'])
#print(lotto)

a = int(input('몇 번이나 뽑을까요? : '))
for i in range(a):
    my_lotto = sorted(random.sample(range(1,46),6))
    print(my_lotto)
    n=0

    for i in my_lotto:
        if i in lotto:
            n += 1


    if n == 6:
        #print("1등입니다~~")
        first += 1
    elif n == 5:
        if response['bnusNo'] in my_lotto:
            #print("2등입니다~~")
            second +=1 
        else:
            #print("3등입니다~~")
            third += 1
    elif n == 4:
        #print("4등입니다~~ 50000원 받아가세요")
        fourth += 1
    elif n == 3:
        #print("5등입니다~~  5000원 받아가세요")
        fifth +=1
    else:
        #print("소중한 천원을 날리셨습니다~")
        bomb +=1

print(f'1등:{first}, 2등:{second}, 3등: {third}, 4등: {fourth}, 5등: {fifth}, 꽝:{bomb}')
if first > 0 :
    print("와~~ 1등이다")

print(f'{2240409000*first + 49420787* second + 1651408* third + 50000 * fourth + 5000*fifth - 1000* a} 원 이득!')