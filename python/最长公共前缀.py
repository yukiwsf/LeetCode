def LongestCommonPrefix(str1, str2):
    ans = ""
    lst = list()
    lst.append(str1)
    lst.append(str2)
    for i in zip(*lst):
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans

if __name__ == '__main__':
    print(LongestCommonPrefix("hallo", "haha"))