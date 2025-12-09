import math

def main():
    width = int((8+3*3)*2+4)
    for i in range(0, 8):
        line = ''
        for j in range(0, i+1):
            x = 2**j
            line = line + str(x).rjust(int(math.log10(2**(7-(i-j))))+1)
            line = line +  " "
        for j in range(i-1, -1, -1):
            x = 2**j
            line = line + str(x).rjust(int(math.log10(2**(7-(i-j))))+1)
            if j is not i:
                line = line + " "
        print(line.center(width))

if __name__ == "__main__":
    main()