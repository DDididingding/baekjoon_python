N = int(input())

for i in range(N):
    tendigit = list(map(int, input().split()))
    tendigit.sort(reverse=True)
    print(tendigit[2])
