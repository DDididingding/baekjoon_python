H, Y = map(int,input().split())
maxmoney = 0

if Y<5:
    if Y<3:
        money = H*(1.05**Y)
        if maxmoney <= money:
            maxmoney = money
    else :
        money = H*(1.2**(Y//3))*(1.05**(Y%3))
        if maxmoney <= money:
            maxmoney = money
else:
    money = H*(1.2**(Y//3))*(1.05**(Y%3))
    if maxmoney <= money:
        maxmoney = money
    
    money = H*(1.)


print(maxmoney)

