s = input('Введите элементы через пробел')
s1 = [int(i) for i in s.split()]
def f(L):
    r = []
    for i in L:
        if i not in r:
            r.append(i)
    return r
print(*f(s1))