
hiddenpics = 0

pic = [[0 for j in range(100)] for i in range(100)]

N, M = map(int,input().split())

for i in range(N):
    paper = list(map(int,input().split()))
    for k in range(paper[0]-1, paper[2]):
        for l in range (paper[1]-1, paper[3]):
            pic[k][l] = pic[k][l] + 1

for i in range(100):
    for j in range(100):
        if pic[i][j] > M:
           hiddenpics = hiddenpics + 1

print(hiddenpics)

    
