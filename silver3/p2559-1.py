N,K = map(int, input().split())

numbers = []
numbers = list(map(int,input().split()))
summation = 0


for i in range(K):
    summation = summation + numbers[i]
    best = summation


for i in range(N - K):
    summation = summation - numbers[i] + numbers[i+K]

    if best < summation:
        best = summation


print(best)
