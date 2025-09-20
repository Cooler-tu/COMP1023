def main():
    x, y = a, b = 1, 2 # 先创造元组(1,2)，再同时赋值给x, y; a, b
    
    #swap
    x, y = y, x
    '''
    is equicalent to 
    tmp = x
    x = y
    y = tmp
    '''

    '''
    is, whether the two things refer to the same objects
    a = 5; b = 5 in some compiler "a is b" will return false
    '''

    a = "Hello World"
    b = "Hello"
    print(b in a) # whether string b is included by a (case-sensitive)
    
    # 3 <= x <= 10 is available

if __name__ == "__main__":
    main()