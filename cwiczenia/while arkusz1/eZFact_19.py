def num_e(epsilon):
    e=2
    i=2
    wyraz=1
    while wyraz >=epsilon:
        wyraz=wyraz*(1/i)
        e=e+wyraz
        i=i+1
    return e
print(num_e(0.000001))