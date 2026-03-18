import random


answer = random.randint(1, 100)
count = 0

print("숫자를 맞혀 보세요. (1 ~ 100)")

while True:
    guess = int(input())
    count += 1

    if guess > answer:
        print("숫자가 너무 큽니다.")
    elif guess < answer:
        print("숫자가 너무 작습니다.")
    else:
        print(f"정답입니다. 숫자는 {answer}입니다. {count}번만에 맞추셨네요!")
        break
