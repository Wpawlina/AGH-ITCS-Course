def lpierwsze(n):
    pierwsza=[1]*(n)
    i=2
    while i*i<=n:
        if pierwsza[i]==1:
            j=i*i
            while j<(n):
                pierwsza[j]=0
                j+=i
        i+=1
    for i in range(2,n):
        if pierwsza[i]==1:
            print(i)


lpierwsze(100)
    
