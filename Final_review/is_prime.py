import numpy as np
import math

vis = np.full((100001, ), False)

def is_prime(x):
    global vis
    for i in range(2, int(math.sqrt(x))+1):
        if vis[i] and x % i == 0:
            return
    vis[x] = True

def main():
    x = int(input("Enter the start of the range: "))
    y = int(input("Enter the end of the range: "))
    global vis
    vis[1] = True
    vis[2] = True
    list = np.arange(0, 100001)
    for i in range(3, y):
        is_prime(i)
    print(list[x:y+1][vis[list[x:y+1]]])


if __name__ == "__main__":
    main()