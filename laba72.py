def f(a):
    if not a:
        return 0, []
    m_l = 1
    m_s = 0
    c_l = 1
    c_s = 0
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            c_l += 1
        else:
            if c_l >m_l:
                m_l = c_l
                m_s = c_s
            c_l = 1
            c_s = i
    if c_l > m_l:
        m_l = c_l
        m_s = c_s
    r = a[m_s : m_s + m_l]
    return m_l, r
a1 = [1, 3, 5, 4, 7, 8, 9, 2]
a2 = [5, 4, 3, 2, 1]
a3 = []
print(f"{a1} -> {f(a1)}") 
print(f"{a2} -> {f(a2)}")   
print(f"{a3} -> {f(a3)}")
         