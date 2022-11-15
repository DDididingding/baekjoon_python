A, B, V = map(int, input().split())

if (V-B)%(A-B) == 0:
    n = (V - B)//(A-B)
else:
    n = (V - B)//(A-B) + 1

print (n)
