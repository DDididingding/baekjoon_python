a= input()
b= input()
c = 0
go = True
C=''
D = ''
for i in range(8):
    
    C = C + str(a[i])
    C = C + str(b[i])



while(go) :
    for i in range(len(C)-1):
        if(int(C[i])+int(C[i+1]) == 0):
            c = 0
        else:
            c = 10%(int(C[i])+int(C[i+1]))
        
        D = D + str(c)
    
    C = D
    if (len(C)==2):
        go = False

print (C)
