def pierwiastek(n):
    suma=0
    liczba=1
    while suma < n:
        suma+=liczba
        liczba+=2
    if suma > n:
        return -1
    return liczba//2

print(pierwiastek(36))