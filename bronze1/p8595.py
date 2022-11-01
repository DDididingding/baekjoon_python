N = int(input())
secretcode = input()
sc = []
hob = 0

for i in range(N):
    if (secretcode[i] >= '0' and secretcode[i] <= '9'):
        if (secretcode[i+1] >= '0' and secretcode[i+1] <= '9'):
            sc.append(secretcode[i])
        else:
            sc.append(secretcode[i])
            hob = hob + int(*sc)
            sc = []

print(hob)
        
