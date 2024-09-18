def ciagRosMal(t):
    rp=t[1]-t[0]
    dl=2
    maxdlr=0
    maxdlm=0
    for i in range(2,len(t)):
        r=t[i]-t[i-1]
        if r==rp:
            dl+=1
        else:
            if dl > maxdlr and r > 0:
                maxdlr=dl
            if dl > maxdlm and r  < 0:
                maxdlm=dl
            dl=2
        rp=r
    return maxdlr-maxdlm
t=[1,2,3,4,3,2]
print(ciagRosMal(t))

       
        

            

