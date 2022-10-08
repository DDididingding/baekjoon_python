x= input()
firstcut = []
secondcut = []
thirdcut = []
dab = []
answer = '~'
for i in range(1, len(x)-1):
    for j in range(i+1,len(x)):
         firstcut = x[:i]
         secondcut = x[i:j]
         thirdcut = x[j::]
         firstcut_r = firstcut[::-1]
         secondcut_r = secondcut[::-1]
         thirdcut_r = thirdcut[::-1]
         dab = firstcut_r + secondcut_r + thirdcut_r
         answer = min(answer,dab)

print(answer)