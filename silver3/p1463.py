x = int(input())
go = True
step = 0
while go:
    if x%3 == 0:
        x = x//3
        step = step + 1
        if x == 1:
            go = False
    elif x%2 == 0:
        x = x//2
        step = step + 1
        if x == 1:
            go = False
    else:
        x = x-1
        step = step + 1
        if x ==1:
            go = False

print (step)
