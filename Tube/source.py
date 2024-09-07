

def volume_tabung(pi, r, t):
    
    v = pi * r**2 * t
    return v

pi = 3.14
r = 3
t = 5
hasil = volume_tabung(pi, r, t)
print(round(hasil, 2))


