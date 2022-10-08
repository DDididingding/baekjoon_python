X = int(input())
go = True
i = 1
add = 0
mother, son = 1, 1
while go:
    if ((i-1)*(i))//2 < X <= ((i)*(i+1))//2:
        add = i + 1
        go = False
    else:
        i = i+1

X = X - ((i-1)*(i))//2

if i%2 == 0:
    son = X
    mother = add - X
else:
    mother = X
    son = add - X

print(son)
print(mother)
print(son, '/', mother, sep='')
print (add)
print(i)
print (X)

