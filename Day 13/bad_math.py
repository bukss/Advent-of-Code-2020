def euclid(a, b):
    s, old_s = 0, 1
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s

    if b != 0:
        bzt = (old_r - old_s * a) // b
    else:
        bzt = 0
    
    return old_s, bzt

def remainder_theorem(a1, n1, a2, n2):
    m1, m2 = euclid(n1, n2)
    x = a1*m2*n2 + a2*m1*n1

    return n1*n2, x%(n1*n2)