import math
import numpy as np

def main():
    x = int(input())
    while x >= 10:
        y = int(0)
        while x > 0:
            y += x % 10
            x //= 10
        x = y
    print(x)


if __name__ == "__main__":
    main()