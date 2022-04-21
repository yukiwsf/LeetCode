import math


def Length(num):
    cnt = 0
    while num:
        num //= 10
        cnt += 1
    return cnt


def IsPalindrome(num):
    if num < 0 or (num != 0 and num % 10 == 0):
        return False
    elif num == 0:
        return True
    else:
        length = int(math.log(num, 10)) + 1
        reverse = 0
        for i in range(length // 2):
            temp = num % 10
            num //= 10
            reverse = reverse * 10 + temp
            if reverse == num or reverse == num // 10:
                return True
            else:
                return False


