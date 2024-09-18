def zad32(T,k):
    n=len(T)
    def rek(i,A,B,dlA,dlB,id):
        if i==n:
            if dlA+dlB==k and A==B and ( dlA!=id or dlB!=id):
                return True
            return False
        return rek(i+1,A+T[i],B,dlA+1,dlB,id) or rek(i+1,A,B+T[i],dlA,dlB+1,id) or rek(i+1,A+T[i],B+T[i],dlA+1,dlB+1,id+1) or rek(i+1,A,B,dlA,dlB,id)
    return rek(0,0,0,0,0,0)