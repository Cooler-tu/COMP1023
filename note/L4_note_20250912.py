import random
# from random import randint # 只导入randint, 调用的时候不用random.randint()，直接randint()
# from random import * # 导入random模块的所有方法, 也不用写random.前缀

def ran():
    a1 = random.random() # float random
    a2 = random.randint(1, 10) # int random 1<=x<=10
    a3 = random.choice([1,2,3,4,5]) # choose from a list
    a4 = random.sample(range(100), 5) # choose multiple from a list (range(100)表示0-99)

    print(a4)

def pri():
    # print(*<object>, sep=' ', end='\n', file=sys.stdout, flush=False)
    # *表示可以打印多个object, sep表示多个object之间的分隔符, end表示输出结束后以什么结尾(默认\n), 
    # file表示打印到哪里, flush表示是否立即刷新输出缓冲区
    
    # 连续表达
    # print(f"<string> {<expression>}")
    x = 18
    print(f"Hello, 我今年刚满{x}岁")

    #换行输出
    print('''hello
world ''') #换行从没有任何缩进算起
    print("hellp \
world") #换行从没有任何缩进算起


if __name__ == "__main__":
    ran()
    pri()
    
    
'''
random的随机数获取方式：通过当前时间得到种子数，再通过种子数生成随机数
'''
