N = int(input())
A = input()
ans = 0

if (N%2 == 0):
    for i in range(N//2):
        if (A[i]!=A[N-i-1]) :
            ans = ans + 1
else :
    for i in range(N//2):
        if (A[i]!=A[N-i-1]) :
            ans = ans + 1

print(ans)



