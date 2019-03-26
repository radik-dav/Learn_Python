import random


# загадать 4-х значное число
def guess_number():
    answers = []
    global answer_num
    for i in range(1000, 10000):
        tmp = str(i)
        if len(set(map(int, tmp))) == 4:
            answers.append(list(map(int, tmp)))
            answer_num = random.choice(answers)


# сравнить числа загаданное компьютером  и введенное пользователем
# и сообщить о количестве быков и коров
def check(nums):
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in answer_num:
            if nums[i] == answer_num[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows
