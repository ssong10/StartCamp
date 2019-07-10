import random
numbers = range(1,46)
for i in range(5):
    이번주일등 = random.sample(numbers,6)
    보너스번호 = random.sample(numbers,1)
    print(sorted(이번주일등), 보너스번호)