N = int(input())
namelist = []
kindlist = []

for i in range(N):
    n = int(input())
    for j in range(n):
        name, kind = input().split()
        namelist.append(name)
        kindlist.append(kind)
    
    