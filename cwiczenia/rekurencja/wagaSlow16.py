def czy_samogloska(ch):
    if ch in ('a','e','y','i','u','o'):
        return 1
    return 0



def wyraz(s1,s2):
    samS1=0
    sumAsciS1=0
    n=len(s2)
    for i in range(len(s1)):
        samS1+=czy_samogloska(s1[i])
        sumAsciS1+=ord(s1[i])
    def rek(i,sumAsci,sam):
        if i==n:
            return sumAsci==sumAsciS1 and sam==samS1
        return rek(i+1,sumAsci,sam) or rek(i+1,sumAsci+ord(s2[i]),sam+czy_samogloska(s2[i]))
    return rek(0,0,0)



