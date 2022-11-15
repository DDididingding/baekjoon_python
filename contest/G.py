T = int(input())
cnt = 0

for i in range(T):
    a ,b = map(int, input().split())
    for i in range(a, b+1):

        cnt = cnt + str(i).count('0')

    print(cnt)
    cnt = 0




