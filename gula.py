

def szamolo(b, c, d):
    d = (b**2 * c)/3
    return int(d)


a = 1
eredmeny = 0

while a != 0:
    a = int(input("Kérem adja meg a gúla alapjának oldalhosszát: "))
    if a != 0:
        m = int(input("Kérem adja meg a gúla magasságát: "))
        print(szamolo(a, m, eredmeny))
