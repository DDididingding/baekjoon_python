import sys
N,K = map(int, input().split())

numbers = []
numbers = sys.stdin.readline().split()
summation = 0
best = int()
for i in range(N-(K-1)):
    for j in range(i,i+K):
        temp = numbers[j]
        temp = int(temp)
        summation = summation + temp
        
    if best < summation:
        best = summation
    
    summation = 0

print (best)    

