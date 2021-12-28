def prime (num):

    b= 0
    for i in  range (1,num):
        if num%i==0:
            b += 1
    if b == 1:
        return(1)
    else:
        return(0)
        
def MA (num):
    global count
    count = 0
    MAlst=[]
    for i in range (1, num):
        if num % i == 0:
            MAlst.append(i)
    for j in MAlst:
        if prime(j) == 1:
            count += 1
    return count       
x = 0
bigestinp = 0
for i in range (0,10):
        inp = int(input())
        m = MA(inp)
        if m > x:
            x = m
            bigestinp = inp
        if m == x:
            if inp > bigestinp:
                bigestinp = inp
            else:
                bigestinp = bigestinp
print(bigestinp,x)
