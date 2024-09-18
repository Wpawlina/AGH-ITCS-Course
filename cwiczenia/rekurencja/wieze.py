def wieze():
    lperm=0
    zajete=[]
    perm=[0]*8
    ile=0
    def rek(i,zajete,perm):
        nonlocal ile
        if i==8:
            ile+=1
            return
        for j in range(1,9):
            if j not in zajete:
                nperm=perm.copy()
                nperm[i]=j
                z2=zajete.copy()
                z2.append(j)
                rek(i+1,z2,nperm)
    rek(0,zajete,perm)
    print(ile)
wieze()


    