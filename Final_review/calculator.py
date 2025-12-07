def cal1(x, k, ans):
    if(len(x) == k):
        return ans
    if(x[k].find('*') != -1):
        s = x[k].split('*')
        ans_m = cal2(s, 0, 1)
        ans += ans_m
    else:
        ans += int(x[k])
    return cal1(x, k+1, ans)

def cal2(x, k, ans):
    if len(x) == k:
        return ans
    return cal2(x, k+1, ans*int(x[k]))


def main():
    s = input()
    x = s.split('+')
    print(cal1(x, 0, 0))


if __name__ == "__main__":
    main()