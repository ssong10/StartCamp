# number.txt를 읽어서

with open('number.txt','r') as file:
    numbers = file.readlines()
print(numbers)

# 리스트를 뒤집니다.
numbers.reverse()

# number_reverse.txt 로 저장!
# 4
# 3
# 2
# 1
# 0
with open('number_reverse.txt','w') as file:
    for number in numbers:
        file.write(number)
