x, y = 0, 0
arrow = 1
M, n = map(int, input().split())
out = False

for i in range(n):

    order = list(input().split())

    if order[0] == 'MOVE':
        if arrow == 1:
            x = x + int(order[1])
        elif arrow == 2:
            y = y + int(order[1])
        elif arrow == 3:
            x = x - int(order[1])
        elif arrow == 4:
            y = y - int(order[1])
    elif order[0] == 'TURN':
        if order[1] == '0':
            if arrow == 4:
                arrow = 1
            else:
                arrow = arrow + 1
        if order[1] == '1':
            if arrow == 1:
                arrow = 4
            else:
                arrow = arrow - 1
    
    if x > M or x < 0:
        out = True
    elif y > M or y < 0:
        out = True

if out == True:
    print(-1)
else:
    print(x,y)

    


