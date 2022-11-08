T = int(input())


for i in range(T):
    N, M = map(int, input().split())

    rows = N
    cols = N
    flight = [[0 for k in range(cols)] for l in range(rows)]

    for j in range(M):
        a, b = map(int, input().split())
        flight[a-1][b-1] = 1
        flight[b-1][a-1] = 1

    

