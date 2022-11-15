pb = []
mother = 1*2*3*4*5*6*7*8*9
totalpb = 1

for i in range(10) :
    pb = pb + input ()

pb = pb.sort(reverse=True)

for i in range(9):
    totalpb =  totalpb * pb[i]



