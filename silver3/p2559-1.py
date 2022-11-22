N,K = map(int, input().split())

numbers = []
numbers = input().split()
summation = 0


for i in range(K):
    temp = numbers[i]
    temp = int(temp)
    summation = summation + temp
    best = summation


for i in range(N - K):
    temp = numbers[i]
    temp = int(temp)
    temp1 = numbers[i+K]
    temp1 = int(temp1)
    summation = summation - temp + temp1

    if best < summation:
        best = summation


print(best)
