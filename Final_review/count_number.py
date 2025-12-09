import math
import numpy as np

def main():
    vis = np.full((105, ), False)
    #试一下换种方式写输入
    # x = input("Enter integers between 1 and 100: ")
    # num_str = np.array(x.split())
    # num_str = np.astype(num_str, int)

    # try 2.0
    num_str = [int(x) for x in input("Hi").split()]
    for i in range(0, len(num_str)):
        vis[num_str[i]] = True
    num_str = list(num_str)
    for i in range(1, 100):
        if vis[i] == True:
            print(f"{i} occurs {num_str.count(i)} time", end="")
            if num_str.count(i) > 1:
                print("s", end="")
            print()


if __name__ == "__main__":
    main()