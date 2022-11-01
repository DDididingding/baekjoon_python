N = int(input())
hakjum = 0
total = 0.0
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-','D+', 'D0', 'D-', 'F']
score1 = [4.3, 4.0 ,3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
for i in range(N):
    sugang = input().split()
    hakjum = hakjum + int(sugang[1])
    total = total + int(sugang[1])*score1[score.index(sugang[2])]

result = total/hakjum

H = result * 1000
H = int(H)
if H%5 == 0:
    result = result+0.001
    
print(round(result,2))
