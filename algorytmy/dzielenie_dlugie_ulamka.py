def ulamek_okresowy(a, b):
    c = a // b
    reszta = a % b
    ułamek = str(c) + "."
    reszty = {}
    pozycja = len(ułamek)
    
    while reszta != 0:
        if reszta in reszty:
            pozycja = reszty[reszta]
            ułamek = ułamek[:pozycja] + "(" + ułamek[pozycja:] + ")"
            break
        reszty[reszta] = pozycja
        a, reszta = divmod(reszta * 10, b)
        ułamek += str(a)
        pozycja += 1
    
    print(reszty)
    return ułamek

a = int(input("Podaj liczbę naturalną a: "))
b = int(input("Podaj liczbę naturalną b (b ≠ 0): "))

if b == 0:
    print("Dzielenie przez zero jest niemożliwe.")
else:
    wynik = ulamek_okresowy(a, b)
    print(f"{a}/{b} = {wynik}")
