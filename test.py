x = 0
x1 = 0
y1 = 0
cnt = 0
for a in range(50):
    for b in range(a, 50):
        if ((2*a+4*b) <=60) and ((2*b+4*a)<=80):
            sum = a*50+b*60
            if sum > x:
                x = sum
                x1 = a
                y1 = b
                cnt += 1
print(x, x1, y1, cnt)

