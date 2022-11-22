import math
N = int(input())

for i in range(N):

    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    d = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    if r1 < r2 :
        r1, r2 = r2, r1

    if d==0:
        if r1 == r2:
            print('-1')
        else:
            print('0')
    elif r1 > d+r2 :
        print('0')
    elif r1 == d+r2 :
        print('1')
    elif r1 < d+r2 :
        if d > (r1+r2):
            print('0')
        elif d == (r1+r2):
            print('1')
        elif d < (r1+r2):
            print('2')

