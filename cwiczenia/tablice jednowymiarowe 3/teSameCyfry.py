def teSameCyfry(num1,num2):
    c1=[0]*10
    c2=[0]*10
    while num1!=0:
        c1[num1%10]+=1
        num1//=10
    while num1!=0:
        c1[num2%10]+=1
        num2//=10
    for i in range(0,10):
        if c1[i]!=c2[i]:
            return False
    return True


