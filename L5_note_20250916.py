def main():
    a, b = 5, 4
    a+b
    a-b
    a*b
    a/b
    a//b # integer division (取整除法)
    # 5.5 / -2 = -3 (-2.75 > -3)
    
    a**b # exponentiation a^b
    # 0 ** 0 == 1
    # 2 ** -1 == 0.5

    a%b
    # a%b = a - a//b
    a = 5.324_4231_4245 # _可以放在数字中间方便计数，但不能1._394
    c = 2 ** 3 ** 2 # from right to left = 2 ** (3**2) = 2 ^ 9
    print(5--6) # or print(5- -6) 负负得正
    '''
    所有带e的科学计数法都是float
    1e0 = 10^0 = 1.0
    '''

if __name__ == "__main__":
    main()