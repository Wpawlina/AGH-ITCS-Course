def zaminana(liczba,system):
    cyfry=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    wynik=''
    while liczba!=0:
        cyfra=liczba%system
        liczba=liczba//system
        wynik=cyfry[cyfra]+wynik
    return wynik
print(zaminana(11,8))