def Reverse(num):
    return str(num)[::-1]


def Reverse1(num):
    l = list()
    if num < 10:
        return num
    while 1:
        if num > 0:
            l.append(str(num % 10))
            num /= 10
            num = int(num)
        else:
            break
    return "".join(l)


print(Reverse(100))
print(Reverse1(99870))