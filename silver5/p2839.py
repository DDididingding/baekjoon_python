N = int(input())
go = True
bag = 0
while go:
    if N%5 == 0:
        bag = bag + N//5
        go = False
    else:
        N = N - 3
        bag = bag + 1
        if N <= 0:
            go = False

if N < 0:
    print('-1')
else:
    print(bag)
    
