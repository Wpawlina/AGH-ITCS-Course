def rosnace_cyfry(n):
    poprzednia_cyfra=10
    while n!=0:
        cyfra=n%10
        n=n//10
        if cyfra >=poprzednia_cyfra:
            return False
        poprzednia_cyfra=cyfra
    return True

print(rosnace_cyfry(7189))