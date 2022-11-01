N = int(input())
go = True

for i in range(N):
    a, b = input().split()
    a = int(a)
    b = int(b)
    a = max(a,b)
    b = min(a,b)
    nam = a % b
    gob = a*b

    while(go) :
        if nam == 0 :
            answer = gob//b
            go = False
            print(answer)
        else:
            temp = nam
            nam = b%nam
            b = temp
    go = True


